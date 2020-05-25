import mongoengine
import datetime
from bson.objectid import ObjectId
from centurio.data.comments import Comment

class AttemptDay(mongoengine.Document):
    day_id = mongoengine.ObjectIdField(required=True, index=True)
    user_id = mongoengine.ObjectIdField(required=True, index=True)
    attempt_id = mongoengine.ObjectIdField(required=True, index=True)
    ordinal = mongoengine.IntField(required=True)
    status = mongoengine.StringField(default='upcoming') #upcoming #complete #past-due
    scheduled_date = mongoengine.DateField(index=True)
    complete_instant = mongoengine.DateTimeField()
    user_description = mongoengine.StringField()
    comments = mongoengine.EmbeddedDocumentListField(Comment)
    likes = mongoengine.ListField()
    #index_date = mongoengine.DateTimeField() - might want to update the indexed_date with the complete instant once it's completed so I can easily search?

meta = {
        'db_alias': 'default',
        'collection': 'attemptdays',
        'indexes': [
            ('-scheduled_date', 'user_id'),
        ]
    }
