import mongoengine
import datetime
import os
import sys
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)
from centurio.data.days import Day


class Project(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    status = mongoengine.IntField(default=1)
    description = mongoengine.StringField()
    link_identifier = mongoengine.StringField(required=True, unique=True)
    creation_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    days = mongoengine.EmbeddedDocumentListField(Day)

    meta = {
        'db_alias': 'default',
        'collection': 'projects'    
    }
