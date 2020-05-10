import mongoengine
import datetime
import os
import sys
from centurio.data.user_info import UserInfo
from centurio.data.user_settings import UserSettings
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

class User(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True, unique=True)
    hashed_pw = mongoengine.StringField(required=True)
    status = mongoengine.IntField(required=True)
    creation_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    end_date = mongoengine.DateTimeField()
    attempts = mongoengine.ListField()
    cohorts = mongoengine.ListField()
    friends_list = mongoengine.ListField()
    user_info = mongoengine.EmbeddedDocumentField(UserInfo)
    user_settings = mongoengine.EmbeddedDocumentField(UserSettings)


    meta = {
        'db_alias': 'default',
        'collection': 'users',    
    }