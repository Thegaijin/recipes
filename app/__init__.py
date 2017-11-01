# app/__init__.py

# Third party import
from flask import Flask
from flask_bootstrap import Bootstrap

# local import
# from config import app_config
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
Bootstrap(app)


''' def create_app(config_name):
    # variable app assigned an instance of class flask
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    Bootstrap(app)
    # temporary route

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app '''


# imported at the end to avoid circular reference
# local import
from app import views
