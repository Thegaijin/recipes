# app/models/yummyApp.py

# Local import
from app.models.users import User

# Third party imports
from flask_login import logout_user
from werkzeug.security import generate_password_hash, check_password_hash


class YummyApp(object):
    ''' Signs up, signs in and signs out users '''

    def __init__(self):
        self.users = {}

    def signup(self, new_user):
        ''' Signs up new users.
        Takes an instance of the User class, checks if the username doesn't
        exist. It adds the user to the users dictionary.

        :param new_user: class instance:
        '''

        if isinstance(new_user, User):
            if new_user.username not in self.users:
                self.users[new_user.username] = new_user
                print("id: {}, username: {}, password: {}".format(
                    new_user.id, new_user.username, new_user.hashed_pswd))
            return True
            return False
        return 'User was not created'
