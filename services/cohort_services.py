from centurio.data.projects import Project
from centurio.data.days import Day
from centurio.data.attempts import Attempt
from centurio.data.users import User
from centurio.data.cohorts import Cohort
from centurio.data.attemptdays import AttemptDay
from centurio.data.comments import Comment
import centurio.services.mongo_setup as mongo_setup
import centurio.services.attempt_services as attempt_service
import centurio.services.user_services as user_service
import datetime
from bson.objectid import ObjectId
# pylint: disable=no-member


def get_cohort_from_id(cohort_id):
    return Cohort.objects(id=cohort_id).first()

def get_cohort_members(cohort_id: ObjectId) -> list:
    return Cohort.objects(id=cohort_id).first().users