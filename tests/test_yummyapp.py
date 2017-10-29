# app/tests/test_yummyapp.py

# third party imports
import pytest

# local imports
from app.models.yummyApp import YummyApp
from app.models.users import User


@pytest.fixture(scope='module')
def user_creator():
    return YummyApp()


def test_yummyapp_paramater_is_instance_of_user(user_creator):
    new_user = User(1, 'username', 'password')
    user_creator.signup(new_user)
    assert isinstance(new_user, User) == True


def test_yummyapp_can_signup_user(user_creator):
    new_user = User(1, 'username', 'password')
    assert user_creator.signup(new_user) == True


def test_yummyapp_cannot_signup_if_user_already_exists(user_creator):
    new_user = User(2, 'username', 'password')
