# app/tests/test_yummyapp.py
''' This script tests the functionality of yummy class '''

# third party imports
from unittest import TestCase

# local imports
from app.models.yummyapp import YummyApp
from app.models.users import User


class YummpyAppTestCase(TestCase):
    '''Testing the methods in the YummyApp class  '''

    def setUp(self):
        self.the_app = YummyApp()
        self.the_users = self.the_app.users
        self.the_user = User('username', 'password')
        self.new_user = User('username', 'password')

    def test_yummyapp_instance(self):
        ''' Test if an instance of YummyApp is created '''

        self.assertIsInstance(self.the_app, YummyApp,
                              msg='Object should be instance of YummyApp')

    def test_yummyapp_user_already_exists(self):
        ''' Test if a username is already taken '''

        self.the_app.signup(self.the_user)
        potential_user = self.the_app.signup(self.new_user)
        self.assertFalse(potential_user, msg='That username already exists')

    def test_yummyapp_user_sign_up(self):
        ''' Test if a user can sign up '''
        self.the_app.signup(self.the_user)
        self.assertIn(self.the_user.username, self.the_users,
                      msg='The user was not able to sign up')

    def test_yummyapp_user_sign_in(self):
        ''' Test if existing user can sign in if their credentials match '''

        self.the_app.signup(self.the_user)
        self.the_app.signin('username', 'password')
        self.assertEqual('password', self.the_users['username'].hashed_pswd,
                         msg='The username and password combination does not \
                        exist')
