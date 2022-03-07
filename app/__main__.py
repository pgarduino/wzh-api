from os import environ

from app import create_app

environment = environ.get("FLASK_ENV", "development")
app = create_app(environment)

if __name__ == '__main__':
    app.run()
