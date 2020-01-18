import flask
from centurio.infrastructure.view_modifiers import response
import centurio.infrastructure.cookie_auth as cookie
import centurio.services.project_services as project_service
from centurio.viewmodels.project.index_viewmodel import IndexViewModel
from centurio.viewmodels.attempt.attempt_viewmodel import AttemptViewModel
from centurio.data.projects import Project
# pylint: disable=no-member

blueprint = flask.Blueprint('attempt', __name__, template_folder='templates')


# ################### ATTEMPT PAGES #################################

@blueprint.route('/attempt/<attempt_id>')
@response(template_file='attempt/attempt.html')
def project_details(attempt_id: str):
    vm = AttemptViewModel(attempt_id)
    if not vm.attempt:
       return flask.abort(status=404)

    return vm.to_dict()

