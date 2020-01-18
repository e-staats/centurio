import mongoengine
import datetime
import os
import sys
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)
from centurio.data.attemptdays import AttemptDay

class Attempt(mongoengine.Document):
    project_id = mongoengine.ObjectIdField(required=True)
    user_id = mongoengine.ObjectIdField(required=True)
    status = mongoengine.StringField(default='in-progress') #abandoned, in-progress, complete
    start_date = mongoengine.DateField(default=datetime.date.today)
    completion_date = mongoengine.DateTimeField()
    attempt_days = mongoengine.DictField()

    meta = {
        'db_alias': 'default',
        'collection': 'attempts'    
    }


    
