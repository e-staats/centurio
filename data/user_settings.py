import mongoengine
import datetime
import os
import sys
from bson.objectid import ObjectId
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

class UserSettings(mongoengine.EmbeddedDocument):
    email_notification = mongoengine.IntField(default=1)