import mongoengine
import datetime

class AttemptDay(mongoengine.Document):
    attempt_id = mongoengine.ObjectIdField(required=True)
    ordinal = mongoengine.IntField(required=True)
    status = mongoengine.IntField(default=1)
    scheduled_day = mongoengine.DateField()
    complete_instant = mongoengine.DateTimeField()

    meta = {
        'db_alias': 'default',
        'collection': 'attempt_days'    
    }