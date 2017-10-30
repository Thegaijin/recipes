# app/tests/test_yummyapp.py

# third party imports
import pytest

# local imports
from app.models.yummyApp import YummyApp
from app.models.users import User


@pytest.fixture(scope='module')
def user_creator():
    return YummyApp()


# FIXME:
