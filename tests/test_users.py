# app/tests/test_users.py

# third party imports
import pytest

# local imports
from app.models.users import User
from app.models.category import category

#######################################################################
#                            CATEGORY TESTS                           #
#######################################################################


@pytest.fixture(scope='module')
def user():
    ''' Returns an instance of the User class '''
    return User(1, "username", "password")


def test_users_is_instance(user):
    """Test if instance of User class is successfully created"""

    assert isinstance(user, User) == True


def test_users_category_raise_error_if_argument_not_string(user):
    ''' Test if the parameter passed to a category is a string '''

    with pytest.raises(TypeError):
        user.create_category(2347)


def test_users_category_doesnt_already_exist(user):
    ''' Test if the category to be created does not already exist '''

    user.create_category("cakes")
    assert "cakes" not in user.categories


def test_users_category_is_created(user):
    ''' Test if the category is created and added to the list '''

    before_length = len(user.categories)
    user.create_category("cakes")
    after_length = len(user.categories)
    x = after_length - before_length
    assert x == 1


def test_users_category_is_viewed(user):
    ''' Test if the category can be viewed '''

    user.create_category("cakes")
    assert user.view_category('cakes') == user.categories['cakes']


def test_if_user_category_can_be_edited(user):
    ''' Test if the category can be edited '''
    user.create_category("cakes")
    user.edit_category("cakes", "bakes")
    # TODO: finish this


def test_if_user_category_can_be_deleted(user):
    ''' Test if categories can be deleted '''
    before_length = len(user.categories)
    user.delete_category("cakes")
    after_length = len(user.categories)
    x = before_length - after_length
    assert x == 1
