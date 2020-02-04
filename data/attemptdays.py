import mongoengine
import datetime
from bson.objectid import ObjectId
from centurio.data.comments import Comment

class AttemptDay(mongoengine.EmbeddedDocument):
    id = mongoengine.ObjectIdField(required=True, default=lambda: ObjectId())
    day_id = mongoengine.ObjectIdField(required=True, index=True)
    ordinal = mongoengine.IntField(required=True)
    status = mongoengine.StringField(default='upcoming') #upcoming #complete #past-due
    scheduled_date = mongoengine.DateField()
    complete_instant = mongoengine.DateTimeField()
    user_description = mongoengine.StringField()
    comments = mongoengine.EmbeddedDocumentListField(Comment)

