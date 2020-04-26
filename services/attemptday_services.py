from centurio.data.projects import Project
from centurio.data.days import Day
from centurio.data.attempts import Attempt
from centurio.data.users import User
from centurio.data.cohorts import Cohort
from centurio.data.attemptdays import AttemptDay
from centurio.data.comments import Comment
import centurio.services.mongo_setup as mongo_setup
import centurio.services.attempt_services as attempt_service
import datetime
from bson.objectid import ObjectId

# pylint: disable=no-member

def get_attempt_day_from_id(attempt_day_id):
    mongo_setup.global_init()
    return AttemptDay.objects(id=attempt_day_id).first()

def get_day_id_from_attempt_day(attempt_day_id):
    mongo_setup.global_init()
    return AttemptDay.objects(id=attempt_day_id).first().day_id