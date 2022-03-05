from flask_restx import Namespace, fields
from flask_restx.inputs import boolean

__all__ = [
    'tasks_ns',
    'tasks_list_parser',
    'tasks_list_response',
    'task_model',
]

tasks_ns = Namespace('tasks', description='API endpoints to handle tasks')

tasks_list_parser = tasks_ns.parser()
tasks_list_parser.add_argument(
    'completed',
    type=boolean,
    help='Filter tasks based on their attribute “completed”. When not specified, returns all tasks.',
    location='args'
)
tasks_list_parser.add_argument(
    'title',
    type=str,
    help='Displays tasks containing the provided string in their title. Defaults to an empty string.',
    location='args'
)
tasks_list_parser.add_argument(
    'user_id',
    type=int,
    help='Filter tasks based on their attribute “user_id”. When not specified, returns all tasks.',
    location='args'
)
tasks_list_response = tasks_ns.model(
    'Task List Response', {
        'total_items': fields.Integer,
        'data:': fields.List(
            fields.Raw(),
            description='List of filter tasks'
        )
    }
)

task_model = tasks_ns.model('Task', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'user_id': fields.Integer(required=True, description='The user id of the task'),
    'title': fields.String(required=True, description='The title of the task'),
    'completed': fields.Boolean(required=True, description='The title of the task'),
})
