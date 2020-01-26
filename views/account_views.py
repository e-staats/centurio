import flask
from centurio.infrastructure.view_modifiers import response
import centurio.infrastructure.cookie_auth as cookie
import centurio.services.user_services as user_service
import centurio.services.project_services as project_service
import centurio.services.attempt_services as attempt_service
from centurio.viewmodels.account.index_viewmodel import IndexViewModel
from centurio.viewmodels.account.register_viewmodel import RegisterViewModel
from centurio.viewmodels.account.login_viewmodel import LoginViewModel
from centurio.data.users import User
# pylint: disable=no-member

blueprint = flask.Blueprint('account', __name__, template_folder='templates')

# ################### INDEX #################################

@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    vm = IndexViewModel()
    if not vm.user_id:
        return flask.redirect('account/login')

    #fake data
    results = vm.to_dict()
    results['day_info']=attempt_service.get_todays_attemptdays_for_user(vm.user_id)
    results['results']={}

    #friends list
    feed_users = user_service.construct_feed_user_list(vm.user)
    for user_id in feed_users:
        user = user_service.find_user_by_id(user_id)
        results['results'][user]=attempt_service.get_todays_attemptdays_for_user(user_id)

    return results

# ################### REGISTER #################################

@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    vm = RegisterViewModel()
    if vm.user_id:
        return flask.redirect('/account')
    return {}


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    vm = RegisterViewModel()
    vm.validate()

    if vm.error:
        return vm.to_dict()
    
    user = user_service.create_user(vm.name,vm.email,vm.password)
    if not user:
        vm.error = "The account could not be created"
        return vm.to_dict()
    
    resp = flask.redirect('/account')
    cookie.set_auth(resp, str(user.id))

    return resp


# ################### LOGIN #################################

@blueprint.route('/account/login', methods=['GET'])
@response(template_file='account/login.html')
def login_get():
    vm = LoginViewModel()
    if vm.user_id:
        return flask.redirect('/account')
    return vm.to_dict()


@blueprint.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():
    vm =LoginViewModel()
    vm.validate()

    if vm.error:
        return vm.to_dict()
    
    #todo: log in browser as session
    resp = flask.redirect('/account')
    cookie.set_auth(resp, str(vm.user.id))

    return resp


# ################### LOGOUT #################################

@blueprint.route('/account/logout')
def logout():
    resp = flask.redirect("/")
    cookie.logout(resp)
    return resp