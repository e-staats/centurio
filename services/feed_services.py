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
from collections import OrderedDict
from bson.objectid import ObjectId
# pylint: disable=no-member


def get_feed_items(user_id,date,index=0,number=10):
     user_set = create_user_set(user_id)
     searching = True
     results = OrderedDict()
     stop = index+number
     while searching:
          activities = AttemptDay.objects(scheduled_date=date,user_id__in=user_set)
          day_results=[]
          for i,activity in enumerate(activities[index:stop]):
               day_results.append(activity.id)
          results[date]=day_results
          if stop_conditions(results,number,date):
               searching=False
          date=date-datetime.timedelta(days=1)
     return results

def stop_conditions(results,number,date):
     if number<=len(results):
          return True
     if max_lookback_days()<=abs((date - datetime.datetime.today()).days):
          return True
     return False

def max_lookback_days():
     return 7

def create_user_set(user_id):
     """
     return set of friends and cohort user ID for a passed in user
     """
     friends = set()
     friends.update(user_service.get_friends(user_id))
     friends.update(user_service.get_cohort_members_for_user(user_id))
     return friends

def get_more_feed_items():
     """
     Design:
     
     """
     pass