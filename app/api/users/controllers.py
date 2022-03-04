from flask_restx import Resource
from http import HTTPStatus
from injector import inject

from app.api.users.serializers import users_ns, user_model, users_list_response
from app.api.tasks.serializers import tasks_list_parser, tasks_list_response

from app.core.filters.filter import Filter
from app.core.filters.condition import Condition

from app.api.users.service import UserService
from app.api.tasks.service import TaskService

@users_ns.route('')
class UsersListController(Resource):
    """ Resource class to handle users """

    @inject
    def __init__(self, service: UserService, **kwargs):
        self.service = service
        super().__init__(**kwargs)

    @users_ns.response(code=HTTPStatus.OK.value, description='Success', model=users_list_response)
    def get(self):
        """ Get all users """
        users = self.service.find_all()
        response = {
            'total_items': len(users),
            'data': users,
        }
        return response, HTTPStatus.OK

@users_ns.route('/<int:user_id>')
@users_ns.response(HTTPStatus.NOT_FOUND, 'User not found')
@users_ns.param('user_id', 'The user identifier')
class UsersController(Resource):

    @inject
    def __init__(self, service: UserService, **kwargs):
        self.service = service
        super().__init__(**kwargs)

    @users_ns.doc('get_user')
    @users_ns.response(HTTPStatus.NOT_FOUND, 'User not found')
    @users_ns.response(code=HTTPStatus.OK.value, description='Success', model=user_model)
    def get(self, user_id: int):
        """ Get Retrieves information from a single task"""
        user = self.service.find(user_id)
        if user is None:
            return "User {} doesn't exist".format(user_id), HTTPStatus.NOT_FOUND
        return user, HTTPStatus.OK

@users_ns.route('/<int:user_id>/tasks')
@users_ns.response(HTTPStatus.NOT_FOUND, 'User not found')
@users_ns.param('user_id', 'The user identifier')
class UsersTasksController(Resource):

    @inject
    def __init__(self, user_service: UserService, task_service: TaskService, **kwargs):
        self.user_service = user_service
        self.task_service = task_service
        super().__init__(**kwargs)

    @users_ns.expect(tasks_list_parser)
    @users_ns.doc('get_tasks_by_user')
    @users_ns.response(HTTPStatus.NOT_FOUND, 'User not found')
    @users_ns.response(code=HTTPStatus.OK.value, description='Success', model=tasks_list_response)
    def get(self, user_id: int):
        """ Retrieves all tasks from the specified user."""
        user = self.user_service.find(user_id)
        if user is None:
            return "User {} doesn't exist".format(user_id), HTTPStatus.NOT_FOUND
        args = tasks_list_parser.parse_args()

        _filter = Filter()
        _filter.add_condition(Condition('user_id', user_id))

        if args.completed is not None:
            _filter.add_condition(Condition('completed', args.completed))
        if args.title:
            _filter.add_condition(Condition('title', args.title, 'contains'))

        tasks = self.task_service.find_all(_filter)
        response = {
            'total_items': len(tasks),
            'data': tasks,
        }
        return response, HTTPStatus.OK
