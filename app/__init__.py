# app/__init__.py
''' This script initialises the app '''

# Third party import
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

# local import

login_manager = LoginManager()
app = Flask(__name__)
app.config.from_object('config')        # Load external config file

Bootstrap(app)


# For user session management and remember the users’ session
login_manager.init_app(app)     # initialise login manager
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "login"


# imported at the end to avoid circular reference
# local import
from app import views
