import flask
from centurio.infrastructure.view_modifiers import response
import centurio.infrastructure.cookie_auth as cookie
import centurio.services.project_services as project_service
from centurio.viewmodels.project.index_viewmodel import IndexViewModel
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
    #project_service._add_project_test()
    #project_service._add_user_attempt_test(vm.user)
    results['projects'] = project_service.get_project_summaries()
    project_service.format_project_list_for_user(results['projects'],vm.user)
    
    #print(results)

    return results

@blueprint.route('/projects', methods=['POST'])
@response(template_file='projects/index.html')
def register_post():
    vm = IndexViewModel()
    # if not vm.user_id:
    #     return vm.to_dict()

    results = vm.to_dict()
    results['projects'] = project_service.get_project_summaries()
    project_service.format_project_list_for_user(results['projects'],vm.user)

    # return resp
    return results

# ################### PROJECT PAGES #################################

@blueprint.route('/projects/<project_link_id>')
@response(template_file='projects/details.html')
def project_details(project_link_id: str):
    vm = ProjectDetailsViewModel(project_link_id)
    if not vm.project:
       return flask.abort(status=404)

    return vm.to_dict()

