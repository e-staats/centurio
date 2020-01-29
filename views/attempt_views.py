import flask
from flask import jsonify
from centurio.infrastructure.view_modifiers import response
import centurio.infrastructure.cookie_auth as cookie
import centurio.services.project_services as project_service
import centurio.services.attempt_services as attempt_service
from centurio.viewmodels.project.index_viewmodel import IndexViewModel
from centurio.viewmodels.attempt.attempt_viewmodel import AttemptViewModel
import centurio.infrastructure.request_dict as request_dict
from centurio.data.projects import Project
# pylint: disable=no-member

blueprint = flask.Blueprint('attempt', __name__, template_folder='templates')


# ################### ATTEMPT PAGES #################################

@blueprint.route('/attempt/<attempt_id>')
@response(template_file='attempt/attempt.html')
def project_details(attempt_id: str):
    vm = AttemptViewModel(attempt_id)
    if not vm.user_id:
        return flask.redirect('account/login')
    if not vm.attempt:
       return flask.abort(status=404)

    return vm.to_dict()


@blueprint.route('/_complete_day', methods=['POST'])
@response(template_file='attempt/attempt.html')
def complete_day():
   request = request_dict.create('')
   attempt_id = request['attempt_id']
   attempt_day_id = request['attempt_day_id']
   user_comment = request['comment']
   print(user_comment)
   updated = attempt_service.complete_day(attempt_id, attempt_day_id)
   if not updated:
      return jsonify(status="error")
   return jsonify(status="success")