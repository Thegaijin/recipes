# app/tests/test_yummyapp.py

# third party imports
import unittest

# local imports
from app.models.yummyApp import YummyApp
from app.models.users import User


class YummpyAppTestCase(unittest.TestCase):
    '''Testing the methods in the YummyApp class  '''


def setUp(self):
    self.the_app = YummyApp()
    self.the_users = self.the_app.users
    self.the_user = User(1, 'username', 'password')


def test_yummyapp_if_instance(self):
    ''' Test if an instance of YummyApp is created '''

    self.assertInstance(self.the_app, YummyApp,
                        msg='Object should be instance of YummyApp')


def test_yummyapp_if_user_already_exists(self):
    ''' Test if a username is already taken '''

    self.new_user = User(2, 'username', 'password')
    self.the_app.signup(self.the_user)
    potential_user = self.the_app.signup(self.new_user)
    self.assertFalse(potential_user, msg='That username already exists')


def test_yummyapp_if_user_can_sign_up(self):
    ''' Test if a user can sign up '''
    self.the_app.signup(self.the_user)
    self.assertIn(self.the_user.username, self.the_users,
                  msg='The user was not able to sign up')


def test_yummyapp_if_user_can_sign_in(self):
    ''' Test if existing user can sign in if their credentials match '''

    self.the_app.signin(self.the_user)
    self.the_app.signin('username', 'password')
    self.assertEqual('password', self.the_users['username'].hashed_pswd,
                     msg='The entered credentials dont match')
