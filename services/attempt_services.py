from centurio.data.projects import Project
from centurio.data.days import Day
from centurio.data.attempts import Attempt
from centurio.data.users import User
from centurio.data.cohorts import Cohort
from centurio.data.attemptdays import AttemptDay
import centurio.services.mongo_setup as mongo_setup
import datetime
# pylint: disable=no-member

def get_attempt_from_id(attempt_id):
    attempt = Attempt.objects(id=attempt_id).first()
    if not attempt:
        return None
    return attempt

def get_todays_attemptdays_for_user(user):
    return day_info_for_timerange(user,datetime.date.today(),datetime.date.today())

def day_info_for_timerange(user,start_date,end_date):
    attempt_list = Attempt.objects().filter(user_id=user.id,start_date__gte=start_date,start_date__lte=end_date)
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