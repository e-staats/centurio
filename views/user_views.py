import flask
from flask import jsonify
from centurio.infrastructure.view_modifiers import response
import centurio.infrastructure.cookie_auth as cookie
import centurio.services.user_services as user_service
import centurio.services.project_services as project_service
import centurio.services.attempt_services as attempt_service
from centurio.viewmodels.user.user_viewmodel import UserViewModel
from centurio.data.users import User
import centurio.infrastructure.request_dict as request_dict
from centurio.data.projects import Project
# pylint: disable=no-member

blueprint = flask.Blueprint('users', __name__, template_folder='templates')

# ################### USER PAGES #################################

@blueprint.route('/users/<user_id>')
@response(template_file='users/user.html')
def user_details(user_id: str):
    vm = UserViewModel(user_id)
    if not vm.user_id:
        return flask.redirect('account/login')

    return vm.to_dict()


@blueprint.route('/_follow', methods=['POST'])
@response(template_file='users/user.html')
def add_friend():
    updated=None
    #request = request_dict.create('')
    if not updated:
        return jsonify(status="error")
    return jsonify(status="success")

