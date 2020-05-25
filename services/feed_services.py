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
import centurio.services.day_services as day_service
import centurio.services.project_services as project_service
import datetime
from collections import OrderedDict
from bson.objectid import ObjectId
# pylint: disable=no-member


def get_feed_items(user_id,date,index=0,number=10):
     user_set = create_user_set(user_id)
     searching = True
     results = OrderedDict()
     while searching:
          attempt_days = AttemptDay.objects(scheduled_date=date,user_id__in=user_set)
          day_results=[]
          stop = index+number
          for i,attempt_day in enumerate(attempt_days[index:stop]):
               day_results.append(format_attempt_day(attempt_day,user_id))
          results[date]=day_results
          if stop_conditions(results,number,date):
               results['index']=i
               results['last_date']=date
               searching=False
          date,index = increment_to_next_day(date,index)
     return results

def stop_conditions(results,number,date):
     if number<=len(results):
          return True
     if max_lookback_days()<=abs((date - datetime.datetime.today()).days):
          return True
     return False

def max_lookback_days():
     return 7

def increment_to_next_day(date,index):
     date=date-datetime.timedelta(days=1)
     index=0
     return date,index

def format_attempt_day(attempt_day,user_id):
     attempt_day_card = {}
     attempt_day_card['id'] = attempt_day.id
     attempt_day_card['prof_pic'] = user_service.get_prof_pic_from_id(attempt_day.user_id)
     attempt_day_card['user_name'] = user_service.get_name_from_id(attempt_day.user_id)
     attempt_day_card['scheduled_date'] = attempt_day.scheduled_date
     attempt_day_card['complete_instant'] = attempt_day.complete_instant
     attempt_day_card['day_name'] = day_service.get_name_from_day_id(attempt_day.day_id)
     attempt_day_card['project_name'] = attempt_service.get_project_name_from_attempt_id(attempt_day.attempt_id)
     attempt_day_card['day_ordinal'] = attempt_day.ordinal
     attempt_day_card['user_description'] = attempt_day.user_description
     attempt_day_card['day_description'] = day_service.get_description_from_day_id(attempt_day.day_id)
     attempt_day_card['comments'] = attempt_day.comments
     attempt_day_card['likes'] = attempt_day.likes
     attempt_day_card['status'] = attempt_day.status
     attempt_day_card['can_complete'] = can_complete(user_id,attempt_day.user_id)
     return attempt_day_card

def can_complete(user_id,attempt_day_user_id):
     if user_id==attempt_day_user_id:
          return 1
     else:
          return 0

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