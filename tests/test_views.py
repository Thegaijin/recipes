# app/tests/test_yummyapp.py
''' This script tests the functionality in the views script '''

# third party imports
from unittest import TestCase

# local imports
from app import app
from app.models.yummyapp import YummyApp
from app.models.users import User
from app.views import (register, signin, logout, create_category,
                       edit_category, view_category, delete_category)


class ViewsTestCase(TestCase):
    # WORK IN PROGRESS:
    def setUp(self):
        DEBUG = False
        self.the_app = app.test_client()
        self.the_user = User('username', 'password')
        self.new_user = User('username', 'password')
        with app.app_context():
            pass

    def test_homepage_loads(self):
        ''' Test if the home page loads '''
        res = register()
        self.assertIn(b'200', res.data)
