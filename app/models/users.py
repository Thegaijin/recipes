# app/models/users.py
''' This script is for creating user class objects '''

# Third party imports
from flask_login import UserMixin


class User(UserMixin):
    ''' The User class is for creating User objects to hold
        the properties of a User
    '''

    def __init__(self, username, hashed_pswd):
        self.username = username
        self.hashed_pswd = hashed_pswd
        self.categories = {}

    def get_id(self):
        """Overriding the id parameter to be username"""

        return self.username
