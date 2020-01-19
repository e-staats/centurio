import mongoengine
import datetime

class AttemptDay(mongoengine.EmbeddedDocument):
    project_id = mongoengine.ObjectIdField(required=True, index=True)
    day_id = mongoengine.ObjectIdField(required=True, index=True)
    ordinal = mongoengine.IntField(required=True)
    status = mongoengine.StringField(default='upcoming') #upcoming #complete #past-due
    scheduled_date = mongoengine.DateField()
    complete_instant = mongoengine.DateTimeField()

    meta = {
        'db_alias': 'default',
        'collection': 'attempt_days'    
    }