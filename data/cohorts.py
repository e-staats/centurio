import mongoengine
import datetime

class Cohort(mongoengine.Document):
    creation_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    project_id = mongoengine.ObjectIdField()
    users = mongoengine.ListField()
    status = mongoengine.IntField(default=1)
    
    meta = {
        'db_alias': 'default',
        'collection': 'cohorts'    
    }
