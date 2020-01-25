from centurio.data.projects import Project
from centurio.data.days import Day
from centurio.data.attempts import Attempt
from centurio.data.users import User
from centurio.data.cohorts import Cohort
from centurio.data.attemptdays import AttemptDay
import centurio.services.mongo_setup as mongo_setup
import centurio.services.attempt_services as attempt_service
import datetime
from bson.objectid import ObjectId
# pylint: disable=no-member

def get_attempt_from_id(attempt_id):
    mongo_setup.global_init()
    attempt = Attempt.objects(id=attempt_id).first()
    if not attempt:
        return None
    return attempt

def check_attempt_status(attempt_id):
    mongo_setup.global_init()
    attempt = Attempt.objects(id=attempt_id).first()
    completed_days = attempt.attempt_days.filter(status='complete')
    if len(completed_days)==len(attempt.attempt_days):
        success = Attempt.objects(id=attempt_id).update(set__status="complete")
        success = Attempt.objects(id=attempt_id).update(set__completion_date=datetime.datetime.now())
        return success
    return None

def get_todays_attemptdays_for_user(user):
    return day_info_for_timerange(user,datetime.date.today(),datetime.date.today())

def day_info_for_timerange(user,start_date,end_date):
    attempt_list = Attempt.objects().filter(user_id=user.id,start_date__lte=end_date)
    date = start_date
    while date >= start_date and date <= end_date:
        results = {}
        for attempt in attempt_list:
            if attempt.status != 'in-progress':
                continue
            project = Project.objects(id=attempt.project_id).first()
            result_dict = get_attempt_info_for_date(attempt,date,project)
            if result_dict:
                results[attempt.id]=result_dict
        date = date + datetime.timedelta(1)
    return results

def get_attempt_info_for_date(attempt,date,project):
    try:
        attempt_days_list = attempt.attempt_days.filter(scheduled_date=date)
    except:
        return

    if not project:
        project = Project.objects(id=attempt.project_id).first()
        if not project:
            return
    
    for attempt_day in attempt_days_list:
        day_id = attempt_day.day_id
        day = Day.objects(id=day_id).first()
        return {"project_name": project.name,
                "ordinal": attempt_day.ordinal,
                "day": day,
                }

def complete_day(attempt_id, day_id):
    mongo_setup.global_init()
    did = ObjectId(day_id)
    success = Attempt.objects(id=attempt_id, attempt_days__id=did).update(set__attempt_days__S__status="complete")
    success = Attempt.objects(id=attempt_id, attempt_days__id=did).update(set__attempt_days__S__complete_instant=datetime.datetime.now())
    if not success:
        return None
    success = check_attempt_status(attempt_id)
    return success

def get_active_attempt_list(user):
    attempts = Attempt.objects(user_id=user.id, status='in-progress')
    return list(attempts)