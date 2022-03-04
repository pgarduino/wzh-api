from flask import Flask
from flask_injector import FlaskInjector
from injector import Injector

import os

from app.api import blueprint as api_blueprint

from app.core.infrastructure.database.json.database import JsonDatabase

from app.config.config import config
from app.config.dependencies import AppModule

# Active endpoints noted as following:
# (blueprint_object)
ACTIVE_ENDPOINTS = (
    api_blueprint,
)

def create_app(environment) -> Flask:
    """Create the Flask APP
    Arguments:
        environment {str} -- Environment (development, testing, production)

    Returns:
        [Flask app] -- The Flask app handler
    """
    app = Flask(__name__)
    # Load configuration based on environment
    app.config.from_object(config[environment])
    # load db
    path = os.path.join(app.root_path, app.config['DB_PATH'])
    db = JsonDatabase(path, ['tasks', 'users'])
    app.db = db
    for blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint)
    # dependency injection framework initialization
    injector = Injector([AppModule(app, db)])
    FlaskInjector(app=app, injector=injector)
    return app
