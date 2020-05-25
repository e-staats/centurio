from flask import Response
import services.mongo_setup as mongo_setup
import datetime
import pprint
import os
import sys
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)
from data.users import User
# pylint: disable=no-member

def primary_user_data():
    return {
        'name': 'primary',
        'email': 'primary@site.com',
        'password': 'Abc123!',
    }

def secondary_user_data():
    return {
        'name': 'secondary',
        'email': 'secondary@site.com',
        'password': 'Abc123!',
    }

def test_feed_items():
    from centurio.services.feed_services import get_feed_items
    mongo_setup.global_init()
    user_id=User.objects.first().id
    date = datetime.datetime.today()
    results = get_feed_items(user_id, date)
    pprint.pprint(results)

if __name__=='__main__':
    test_feed_items()