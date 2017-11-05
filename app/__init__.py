# app/__init__.py

# Third party import
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

# local import
# from config import app_config
login_manager = LoginManager()
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

Bootstrap(app)


# For user session management and remember the users’ session
login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "login"


''' def create_app(config_name):
    # variable app assigned an instance of class flask
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    Bootstrap(app)

    # For user session management and remember the users’ session
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "login"

    return app '''


# imported at the end to avoid circular reference
# local import
from app import views
