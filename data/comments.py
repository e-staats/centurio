import mongoengine
import datetime
from bson.objectid import ObjectId

class Comment(mongoengine.EmbeddedDocument):
    id = mongoengine.ObjectIdField(required=True, default=lambda: ObjectId())
    attemptday_id = mongoengine.ObjectIdField(required=True, index=True)
    status = mongoengine.StringField(default='active') #active #deleted
    post_instant = mongoengine.DateTimeField(default=datetime.datetime.now)
    user_id = mongoengine.ObjectIdField()
    text = mongoengine.StringField()
