from centurio.data.projects import Project
from centurio.data.days import Day
from centurio.data.attempts import Attempt
from centurio.data.users import User
from centurio.data.cohorts import Cohort
from centurio.data.attemptdays import AttemptDay
from centurio.data.comments import Comment
import centurio.services.mongo_setup as mongo_setup
import centurio.services.attemptday_services as attemptday_service
import datetime
from bson.objectid import ObjectId

# pylint: disable=no-member


def get_attempt_from_id(attempt_id):
    mongo_setup.global_init()
    attempt = Attempt.objects(id=attempt_id).first()
    if not attempt:
        return None
    return attempt

def get_project_name_from_attempt_id(attempt_id):
    attempt = Attempt.objects(id=attempt_id).first()
    if not attempt:
        return None
    project_name = Project.objects(id=attempt.project_id).first().name
    if not project_name:
        return None
    return project_name


def check_attempt_status(attempt_id):
    mongo_setup.global_init()
    if len(
        AttemptDay.objects().filter(attempt_id=attempt_id, status="complete")
    ) == len(AttemptDay.objects().filter(attempt_id=attempt_id)):
        return None
    success = Attempt.objects(id=attempt_id).update(set__status="complete")
    success = Attempt.objects(id=attempt_id).update(
        set__completion_date=datetime.datetime.now()
    )
    return success


def get_todays_attemptdays_for_user(user_id):
    return day_info_for_timerange(user_id, datetime.date.today(), datetime.date.today())


def day_info_for_timerange(user_id, start_date, end_date):
    attempt_list = Attempt.objects().filter(
        user_id=user_id, start_date__lte=end_date, status="in-progress"
    )
    date = start_date
    while date >= start_date and date <= end_date:
        results = {}
        for attempt in attempt_list:
            project = Project.objects(id=attempt.project_id).first()
            result_dict = get_attempt_info_for_date(attempt, date, project)
            if result_dict:
                results[attempt.id] = result_dict
        date = date + datetime.timedelta(1)
    return results


def get_attempt_info_for_date(attempt, date, project):
    try:
        attempt_days_list = AttemptDay.objects(attempt_id=attempt.id,scheduled_date=date)
    except:
        return

    if not project:
        project = Project.objects(id=attempt.project_id).first()
        if not project:
            return

    for attempt_day in attempt_days_list:
        day_id = attempt_day.day_id
        day = Day.objects(id=day_id).first()
        return {
            "project_name": project.name,
            "attempt_day": attempt_day,
            "day": day,
        }


def complete_day(attempt_id, day_id, comment):
    mongo_setup.global_init()
    attemptday_id = ObjectId(day_id)
    success = AttemptDay.objects(id=attemptday_id).update(
        set__status="complete",
        set__complete_instant=datetime.datetime.now(),
        set__user_description=comment,
    )
    # success = AttemptDay.objects(id=attemptday_id).update(set__complete_instant=datetime.datetime.now())
    # success = AttemptDay.objects(id=attemptday_id).update(set__user_description=comment)
    if not success:
        return None
    success = check_attempt_status(attempt_id)
    return success


def get_active_attempt_list(user):
    attempts = Attempt.objects(user_id=user.id, status="in-progress")
    return list(attempts)


def add_comment(attempt_id, day_id, user_comment, user_id):
    mongo_setup.global_init()
    attemptday_id = ObjectId(day_id)
    comment = Comment()
    comment.attemptday_id = attemptday_id
    comment.user_id = user_id
    comment.text = user_comment

    success = AttemptDay.objects(id=attemptday_id).update_one(push__comments=comment)

    return success
