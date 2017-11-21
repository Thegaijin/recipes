# app/tests/test_yummyapp.py
''' This script tests the functionality in the views script '''

# third party imports
from flask import Flask
from flask_testing import TestCase
from werkzeug.security import generate_password_hash

# local imports
from app import app
from app.models.yummyapp import YummyApp
from app.models.users import User
from app.views import (register, signin, logout, create_category,
                       edit_category, view_category, delete_category)


class ViewsTestCase(TestCase):
    # WORK IN PROGRESS:
    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        DEBUG = False
        self.the_app = app.test_client()
        self.user = YummyApp()
        self.hsh_pswd = generate_password_hash('password')
        self.the_user = User('username', self.hsh_pswd)
        # self.new_user = User('username', 'hsh_pswd')

    def test_homepage_loads(self):
        ''' Test if the home page loads '''
        # res = register()
        # self.assertIn(b'200', res.data)
        res = self.the_app.get('/', follow_redirects=True)
        self.assertIn(b'Sign Up', res.data)

    ''' def test_user_registration(self):
        Test if user can register
        with self.the_app as client:
            res = client.post('/', data=dict(username='username',
                                             password='password'),
                              follow_redirects=True)
            self.assertEqual(res.status_code, 200)
            print(res.data) '''

    def test_user_registration(self):
        ''' Test if user can register '''

        self.user.signup(self.the_user)
        res = self.the_app.post('/', data={'username': 'username',
                                           'password': 'password'},
                                follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        ''' self.assertIn(b'username, Your account has been created', res.data)
        self.assert_redirects(res, url_for('login'))
        '''
    ''' def test_user_login(self):
        Test if user can login
        with self.the_app as client:
            res = client.post('/login/', data=dict(username='username',
                                                   password='password'),
                              follow_redirects=True) '''

    ''' def test_user_create_category(self):
        Test if user can create a category
        res = self.the_app.post('/create_category/', follow_redirects=True)
    '''
