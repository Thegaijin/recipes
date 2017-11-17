# app/tests/test_yummyapp.py
''' This script tests the functionality in the views script '''

# third party imports
from unittest import TestCase
from werkzeug.security import generate_password_hash

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
        user = YummyApp()
        hsh_pswd = generate_password_hash('password')
        # self.the_user = User('username', 'password')
        # self.new_user = User('username', 'password')
        ''' with app.app_context():
            pass '''

    def test_homepage_loads(self):
        ''' Test if the home page loads '''
        # res = register()
        # self.assertIn(b'200', res.data)
        res = self.the_app.get('/', follow_redirects=True)
        self.assertIn(b'Sign Up', res.data)

    def test_user_registration(self):
        ''' Test if user can register '''
        # register()
        res = self.the_app.post('/', follow_redirects=True)
        # print(res)
        # self.assertIn(b'Your account has beeb created', res.data)

    def test_user_login(self):
        ''' Test if user can login '''
        res = self.the_app.post('/login/', follow_redirects=True)

    def test_user_create_category(self):
        ''' Test if user can create a category '''
        res = self.the_app.post('/create_category/', follow_redirects=True)
