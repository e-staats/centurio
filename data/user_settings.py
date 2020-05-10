import mongoengine
import datetime
from bson.objectid import ObjectId

class UserSettings(mongoengine.EmbeddedDocument):
    email_notification = mongoengine.IntField(default=1)