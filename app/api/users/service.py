from app.api.users.repository import UserRepository

class UserService:
    """
        Represents a user service.
    """
    def __init__(self, repository: UserRepository):
        """
            Constructor user service.

            :param repository: The user repository
        """
        self.repository = repository

    def find_all(self):
        """
            Get all users
        """
        return self.repository.find_all()

    def find(self, _id: int):
        """
            Get user by id

            :param _id: The identifier of user
        """
        return self.repository.find(_id)