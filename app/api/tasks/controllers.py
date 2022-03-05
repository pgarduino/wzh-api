from flask_restx import Resource
from http import HTTPStatus
from injector import inject

from app.api.tasks.serializers import tasks_ns, tasks_list_parser, tasks_list_response, task_model

from app.core.filters.filter import Filter
from app.core.filters.condition import Condition

from app.api.tasks.service import TaskService

@tasks_ns.route('')
class TasksListController(Resource):
    """ Resource class to handle tasks """

    @inject
    def __init__(self, service: TaskService, **kwargs):
        self.service = service
        super().__init__(**kwargs)

    @tasks_ns.expect(tasks_list_parser)
    @tasks_ns.response(code=HTTPStatus.OK.value, description='Success', model=tasks_list_response)
    def get(self):
        """ Get all of filtered tasks """
        args = tasks_list_parser.parse_args()

        _filter = Filter()
        if args.completed is not None:
            _filter.add_condition(Condition('completed', args.completed))
        if args.title:
            _filter.add_condition(Condition('title', args.title, 'contains'))
        if args.user_id:
            _filter.add_condition(Condition('user_id', args.user_id))

        tasks = self.service.find_all(_filter)
        response = {
            'total_items': len(tasks),
            'data' : tasks,
        }
        return response, HTTPStatus.OK

@tasks_ns.route('/<int:id>')
@tasks_ns.response(HTTPStatus.NOT_FOUND, 'Task not found')
@tasks_ns.param('id', 'The task identifier')
class TasksController(Resource):

    @inject
    def __init__(self, service: TaskService, **kwargs):
        self.service = service
        super().__init__(**kwargs)

    @tasks_ns.doc('get_task')
    @tasks_ns.response(HTTPStatus.NOT_FOUND, 'Task not found')
    @tasks_ns.response(code=HTTPStatus.OK.value, description='Success', model=task_model)
    def get(self, id: int):
        """ Get Retrieves information from a single task"""
        task = self.service.find(id)
        if task is None:
            return "Task {} doesn't exist".format(id), HTTPStatus.NOT_FOUND
        return task, HTTPStatus.OK
