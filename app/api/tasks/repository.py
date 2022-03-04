from app.core.filters.filter import Filter

from app.core.infrastructure.database.json.database import JsonDatabase

class TaskRepository:
    """
        Represents a task repository.
    """
    def __init__(self, db: JsonDatabase) -> None:
        """
            Constructor task repository.

            :param db: The json database
        """
        self.db = db

    def find_all(self):
        """
            Retrieve all tasks
        """
        return self.db.collection('tasks').all()

    def find_by(self, _filter: Filter):
        """
            Retrieve all the tasks of a user based on filter

            :param _filter: The filter to find tasks
        """
        return self.db.collection('tasks').search(_filter)

    def find(self, _id: int):
        """
            Retrieve task by id

            :param _id: The identifier of task
        """
        return self.db.collection('tasks').get(_id)

