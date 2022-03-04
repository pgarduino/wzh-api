from flask import Flask
from injector import Module, singleton

from app.core.infrastructure.database.json.database import JsonDatabase
from app.api.tasks.repository import TaskRepository
from app.api.users.repository import UserRepository
from app.api.tasks.service import TaskService
from app.api.users.service import UserService

class AppModule(Module):
    def __init__(self, app: Flask, db: JsonDatabase):
        self.app = app
        self.db = db

    def configure(self, binder):
        task_repository = TaskRepository(self.db)
        task_service = TaskService(task_repository)

        user_repository = UserRepository(self.db)
        user_service = UserService(user_repository)

        binder.bind(TaskService, to=task_service, scope=singleton)
        binder.bind(UserService, to=user_service, scope=singleton)
