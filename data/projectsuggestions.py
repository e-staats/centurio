import mongoengine
import datetime
import os
import sys
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

class ProjectSuggestion(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    status = mongoengine.IntField(default=1)
    description = mongoengine.StringField()
    submitting_user = mongoengine.ObjectIdField(required=True)
    creation_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    suggested_days = mongoengine.ListField()

    meta = {
        'db_alias': 'default',
        'collection': 'project_suggestions'    
    }
