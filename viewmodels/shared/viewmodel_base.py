import flask
from flask import Request
import centurio.infrastructure.request_dict as request_dict
import centurio.infrastructure.cookie_auth as cookie
import centurio.services.user_services as user_service
import bson

from typing import Optional

class ViewModelBase:
    def __init__(self):
        self.request: Request = flask.request
        self.request_dict = request_dict.create('')

        self.error: Optional[str] = None
        self.user_id:  Optional[bson.ObjectId] = cookie.get_user_id_via_auth_cookie(self.request)
        if self.user_id:
            self.user = user_service.find_user_by_id(self.user_id)
            self.user_name = self.user.name

    def to_dict(self):
        return self.__dict__
