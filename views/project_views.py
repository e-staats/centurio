import flask
from flask import jsonify
from centurio.infrastructure.view_modifiers import response
import centurio.infrastructure.cookie_auth as cookie
import centurio.services.project_services as project_service
import centurio.services.project_suggestion_services as project_suggestion_service
from centurio.viewmodels.project.index_viewmodel import IndexViewModel
from centurio.viewmodels.project.submit_viewmodel import SubmitViewModel
from centurio.viewmodels.project.details_viewmodel import ProjectDetailsViewModel
from centurio.data.projects import Project
# pylint: disable=no-member

blueprint = flask.Blueprint('project', __name__, template_folder='templates')

# ################### INDEX #################################

@blueprint.route('/projects')
@response(template_file='projects/index.html')
def index():
    vm = IndexViewModel()
    # if not vm.user_id:
    #     return vm.to_dict()

    results = vm.to_dict()
    results['projects'] = project_service.get_project_summaries()
    project_service.format_project_list_for_user(results['projects'],vm.user)
    
    #print(results)

    return results

@blueprint.route('/_attempt_project', methods=['POST'])
@response(template_file='projects/index.html')
def attempt_project():
    vm = IndexViewModel()
    if vm.error:
        return vm.to_dict()
    attempt_id = str(project_service.add_project_to_user(vm.user, vm.link_identifier))
    if not attempt_id:
        return jsonify(status="error", message=vm.error)
    return jsonify(status="success", redirect_url=f"/attempt/{attempt_id}")

@blueprint.route('/_make_test_projects', methods=['POST'])
@response(template_file='projects/index.html')
def make_test_projects():
    vm = IndexViewModel()
    if vm.error:
        return vm.to_dict()
    project_service._add_project_test()
    return jsonify(status="success", redirect_url="/projects")

# ################### PROJECT PAGES #################################

@blueprint.route('/projects/<project_link_id>')
@response(template_file='projects/details.html')
def project_details(project_link_id: str):
    vm = ProjectDetailsViewModel(project_link_id)
    if not vm.project:
       return flask.abort(status=404)

    return vm.to_dict()

# ################### SUBMIT IDEA #################################

@blueprint.route('/projects/submit', methods=['GET'])
@response(template_file='projects/submit.html')
def submit_idea():
    vm = SubmitViewModel()
    if not vm.user_id:
        return flask.redirect('account/login')
    if vm.error:
        return vm.to_dict()

    return vm.to_dict()

@blueprint.route('/projects/submit', methods=['POST'])
@response(template_file='projects/submit.html')
def register_post():
    vm = SubmitViewModel()
    if not vm.user_id:
        return flask.redirect('account/login')
    vm.validate()

    if vm.error:
        return vm.to_dict()
    
    project_suggestion_service.add_project_suggestion(vm)
    if vm.error:
        return vm.to_dict()

    return vm.to_dict()

