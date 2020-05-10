import flask
import sys
import os
from centurio.infrastructure.view_modifiers import response
from centurio.viewmodels.home.index_viewmodel import IndexViewModel
from flask import jsonify

blueprint = flask.Blueprint('home', __name__, template_folder='templates')

@blueprint.route('/', methods=['GET', 'POST'])
@response(template_file="home/index.html")
def index():
    vm = IndexViewModel()
    return vm.to_dict()

@blueprint.route('/about', methods=['GET'])
@response(template_file="home/about.html")
def about():
    vm = IndexViewModel()
    return vm.to_dict()

@blueprint.route('/todo', methods=['GET'])
@response(template_file="home/todo.html")
def todo():
    vm = IndexViewModel()
    return vm.to_dict()

@blueprint.route('/_test', methods=['GET'])
@response(template_file="home/index.html")
def test():
    return jsonify(status="hello from Flask")