from http import HTTPStatus

from . import BaseTestClass

class TasksControllerTestCase(BaseTestClass):

    def test_list_tasks_success(self):
        res = self.client.get('/api/tasks')
        self.assertEqual(HTTPStatus.OK, res.status_code)

    def test_list_tasks_with_filter_success(self):
        res = self.client.get('/api/tasks?completed=true&title=baa')
        self.assertEqual(HTTPStatus.OK, res.status_code)

    def test_list_tasks_with_filter_bad_request(self):
        res = self.client.get('/api/tasks?completed=bad')
        self.assertEqual(HTTPStatus.BAD_REQUEST, res.status_code)

    def test_get_task_success(self):
        res = self.client.get('/api/tasks/1')
        self.assertEqual(HTTPStatus.OK, res.status_code)

    def test_get_task_not_found(self):
        res = self.client.get('/api/tasks/id-not-found')
        self.assertEqual(HTTPStatus.NOT_FOUND, res.status_code)
