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
                return True
            return False
        return 'User was not created'

    def signin(self, username, password):
        """Signs in existing users.
        Takes in 2 parameters. Check is the username exists in users.Checks if the 
        entered password matches the credentials saved with the username

        :param username: A string:
        :param password:
        """
        # check if username exists
        if username in self.users:
            # check if password matches the value of the username key
            hash_pswd = self.users[username].hashed_pswd
            if check_password_hash(hash_pswd, password):
                # return that users instance
                return self.users[username]
            return "The username and password combination \
                        does not exist"
        return "The username does not exist, please signup"

    def logout(self, username):
        """Signs out the currently logged in user

        :param username: A string:
        """
        return "The user was logged out"
