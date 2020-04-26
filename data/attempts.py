import mongoengine
import datetime
import os
import sys
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

class Attempt(mongoengine.Document):
    project_id = mongoengine.ObjectIdField(required=True)
    user_id = mongoengine.ObjectIdField(required=True)
    name = mongoengine.StringField(required=True)
    status = mongoengine.StringField(default='in-progress') #abandoned, in-progress, complete
    start_date = mongoengine.DateField(default=datetime.date.today)
    completion_date = mongoengine.DateTimeField()
    attempt_days = mongoengine.ListField()
    cohort_id = mongoengine.ObjectIdField()

    meta = {
        'db_alias': 'default',
        'collection': 'attempts',
        'indexes': [
            ('-attempt_days.scheduled_date', 'user_id')
        ]
    }



    
