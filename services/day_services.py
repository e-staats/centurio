from centurio.data.projects import Project
from centurio.data.days import Day
from centurio.data.attempts import Attempt
from centurio.data.users import User
from centurio.data.cohorts import Cohort
from centurio.data.attemptdays import AttemptDay
import centurio.services.mongo_setup as mongo_setup
import datetime
# pylint: disable=no-member

def get_day_from_id(day_id):
    day = Day.objects(id=day_id).first()
    return day

def get_description_from_day_id(day_id):
    day = Day.objects(id=day_id).first()
    return day.description