import mongoengine
import datetime
import os
import sys
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)
from centurio.data.user_settings import UserSettings
from centurio.services.user_creation_services import assign_default_prof_pic


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
    user_settings = mongoengine.EmbeddedDocumentField(UserSettings)
    prof_pic_url = mongoengine.StringField(default=assign_default_prof_pic)
    location = mongoengine.StringField()
    bio = mongoengine.StringField()
    social_media_link = mongoengine.StringField()


    meta = {
        'db_alias': 'default',
        'collection': 'users',    
    }