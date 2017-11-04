# app/tests/test_yummyapp.py

# third party imports
import pytest
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
