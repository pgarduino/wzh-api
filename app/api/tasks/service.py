from app.core.filters.filter import Filter

from app.api.tasks.repository import TaskRepository

class TaskService:
    """
        Represents a task service.
    """
    def __init__(self, repository: TaskRepository):
        """
            Constructor task service.

            :param repository: The task repository
        """
        self.repository = repository

    def find_all(self, _filter: Filter = None):
        """
            Get all of filtered tasks

            :param _filter: the filter to fetch the tasks
        """
        if _filter is None or not _filter.conditions:
            return self.repository.find_all()

        return self.repository.find_by(_filter)

    def find(self, _id: int):
        """
            Get task by id

            :param _id: The identifier of task
        """
        return self.repository.find(_id)
