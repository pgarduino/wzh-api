import unittest

from app.core.filters.filter import Filter
from app.core.filters.condition import Condition

class FiltersTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_filter_tasks_when_completed(self):
        tasks = [
            {'id': 1, 'title': 'dummy-title-1', 'completed': True},
            {'id': 2, 'title': 'dummy-title-2', 'completed': False}
        ]
        tasks_expected = [
            {'id': 1, 'title': 'dummy-title-1', 'completed': True},
        ]
        f = Filter()
        f.add_condition(Condition('completed', True))
        tasks_filtered = list(filter(f, tasks))
        self.assertEqual(tasks_filtered, tasks_expected)

    def test_filter_tasks_when_title_contains(self):
        tasks = [
            {'id': 1, 'title': 'bla dummy title task 1', 'completed': True},
            {'id': 2, 'title': 'bla dummy title task 2', 'completed': False},
            {'id': 3, 'title': 'lorem sim', 'completed': True},
        ]
        tasks_expected = [
            {'id': 1, 'title': 'bla dummy title task 1', 'completed': True},
            {'id': 2, 'title': 'bla dummy title task 2', 'completed': False}
        ]
        f = Filter()
        f.add_condition(Condition('title', 'dummy title', 'contains'))
        tasks_filtered = list(filter(f, tasks))
        self.assertEqual(tasks_filtered, tasks_expected)

    def test_filter_tasks_when_completed_and_title_contains(self):
        tasks = [
            {'id': 1, 'title': 'bla dummy title task 1', 'completed': True},
            {'id': 2, 'title': 'bla dummy title task 2', 'completed': False},
            {'id': 3, 'title': 'lorem sim', 'completed': True},
        ]
        tasks_expected = [
            {'id': 1, 'title': 'bla dummy title task 1', 'completed': True},
        ]
        f = Filter()
        f.add_condition(Condition('completed', True))
        f.add_condition(Condition('title', 'dummy title', 'contains'))
        tasks_filtered = list(filter(f, tasks))
        self.assertEqual(tasks_filtered, tasks_expected)




