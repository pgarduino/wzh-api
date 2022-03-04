from flask import Blueprint
from flask_restx import Api

from app.api.tasks.controllers import tasks_ns
from app.api.users.controllers import users_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint, title='Wzh RestAPI',
    description='Serving app for Wzh',
    version='1.0'
)

api.add_namespace(tasks_ns, "/api/tasks")
api.add_namespace(users_ns, "/api/users")
