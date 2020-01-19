import mongoengine
import datetime

class Day(mongoengine.Document):
    day_id = mongoengine.IntField()
    name = mongoengine.StringField(required=True)
    status = mongoengine.IntField(default=1)
    ordinal = mongoengine.IntField(required=True)
    description = mongoengine.StringField()
    creation_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    est_minutes = mongoengine.IntField()
