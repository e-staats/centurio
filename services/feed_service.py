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


def get_feed_items(user_id,timestamp,number):
     user_set = create_user_set(user_id)
     #activities = AttemptDay.find({scheduled_date__$lt__timestamp, user_id in user_set }).limit(number)
     pass

def create_user_set(user_id):
     """
     Design:
     return list of friends and cohort user ID for a passed in user
     """
     friends = {}
     friends.update(user_service.get_friends(user_id))
     friends.update(user_service.get_cohort_members_for_user(user_id))
     return friends

def get_more_feed_items():
     """
     Design:
     
     """
     pass