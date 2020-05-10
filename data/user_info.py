import mongoengine
import datetime
from centurio.services.user_creation_services import assign_default_prof_pic

class UserInfo(mongoengine.EmbeddedDocument):
    prof_pic_url = mongoengine.StringField(default=assign_default_prof_pic)
    location = mongoengine.StringField()
    bio = mongoengine.StringField()
    social_media_link = mongoengine.StringField()
