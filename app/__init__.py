# app/__init__.py

# Third party import
from flask import Flask

# local import
from config import app_config


def create_app(config_name):
    # variable app assigned an instance of class flask
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app


# import at the end to avoid circular reference
# local import
''' from app import views '''
