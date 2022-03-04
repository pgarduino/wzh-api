from app.core.infrastructure.database.json.database import JsonDatabase

class UserRepository:
    """
        Represents a user repository.
    """
    def __init__(self, db: JsonDatabase):
        """
            Constructor user repository.

            :param db: The json database
        """
        self.db = db

    def find_all(self):
        """
            Retrieve all users
        """
        return self.db.collection('users').all()

    def find(self, _id: int):
        """
            Retrieve user by id

            :param _id: The identifier of user
        """
        return self.db.collection('users').get(_id)
