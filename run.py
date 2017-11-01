# run.py
# Third party import
# import os

# Local import
from app import app
''' from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name) '''

if __name__ == '__main__':
    app.run(debug=True)
