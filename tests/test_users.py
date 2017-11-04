# app/tests/test_users.py

# third party imports
import pytest

# local imports
from app.models.users import User
from app.models.category import Category

#######################################################################
#                            CATEGORY TESTS                           #
#######################################################################


@pytest.fixture(scope='module')
def new_user():
    ''' Returns an instance of the User class '''
    return User()


@pytest.fixture(scope='module')
def category():
    ''' Returns a category '''
    category_a = User().create_category('bakes')
    return category_a


########################### REFACTOR TO UNITTEST  ##########################


class UserTestCase(unittest.TestCase):
    ''' Testing the functionality of the methods in the User Class '''

    def setUp(self):
        self.the_user = User(1, 'username', 'password')
        self.categories = self.the_user.categories

    def test_user_is_instance(self):
        """Test if instance of User class is successfully created"""

        # assert isinstance(new_user, User) is True
        self.assertIsInstance(self.the_user, User,
                              msg='Object should be instance of User class')

    def test_user_if_category_doesnt_already_exist(self):
        ''' Test if the category to be created doesn\'t already exist '''

        self.the_user.create_category(1, "cakes", 'dough on dough on dough')
        assert "cakes" not in self.the_user.categories

    def test_user_if_category_can_be_created(self):
        ''' Test if the category is created and added to the list '''

        self.the_user.create_category(1, "cakes", 'baked goods')
        self.assertIn('cakes', self.the_user.categories,
                      msg='The category was not added')

    def test_user_if_category_can_be_viewed(self):
        ''' Test if the category can be viewed '''

        self.the_user.create_category(1, "cakes", 'baked goods')
        viewed = self.the_user.view_category("cakes")
        self.assertEqual('cakes', viewed.category_name,
                         msg='A category by that name doesn\'t exist')

    def test_user_if_category_can_be_edited(self):
        ''' Test if the category can be edited '''

        self.the_user.create_category(1, "cakes", 'baked goods')
        edited = self.the_user.edit_category("cakes", 'dough on dough')
        self.assertEqual('dough on dough',
                         edited['cakes'].description,
                         msg='The category description wasn\'t edited')


def test__user_if_category_can_be_deleted(self):
    ''' Test if categories can be deleted '''

    self.the_user.create_category(1, "cakes", 'baked goods')
    deleted = self.the_user.delete_category("cakes")
    self.assertFalse('cakes', deleted,
                     msg='The category was not deleted')

#######################################################################
#                              RECIPE TESTS                           #
#######################################################################


@pytest.mark.parametrize('recipe_name', [1, [1, 2], 100.1, -5])
def test_users_recipe_error_if_not_string(new_user, category, recipe_name):
    ''' Test if the parameter passed to a recipe is a string '''
    with pytest.raises(TypeError):
        new_user.create_recipe(category, 'recipe_name')
        # TODO: finish me or delete me


def test_users_recipe_doesnt_already_exist(new_user):
    ''' Test if the category to be created does not already exist '''

    new_user.create_recipe("cakes", "cupcakes")
    assert "cupcakes" not in new_user.categories['cakes']


''' def test_if_users_recipe_is_created(new_user, category):
    Test if the recipe is created and added to the list

    pre_length = len(new_user.categories['cakes'])
    new_user.create_recipe('cakes', 'cupcake')
    post_length = len(new_user.categories['cakes'])
    x = post_length - pre_length
    assert x == 1
    assert 'cupcakes' in new_user.categories['cakes']


def test_if_users_recipes_is_viewed(new_user, category):
    Test if the recipe can be viewed
    viewed = new_user.view_recipe('cakes', 'cupcakes')
    assert 'cupcakes' in new_user.categories['cakes']
    # FIXME: Not clear, cross check in the morning


def test_users_edit_recipes(new_user, category):
    Test if the recipe can be edited 
    new_user.edit_recipe('cakes', 'cupcakes')
    # TODO:


def test_user_can_delete_recipe(new_user, category):
    Test if a recipe can be deleted from a category 
    pre_length = len(new_user.categories['cakes'])
    new_user.delete_recipe("cakes", "cupcakes")
    post_length = len(new_user.categories['cakes'])
    x = pre_length - post_length
    assert x == 1
    assert 'cupcakes' not in new_user.categories['cakes'] '''
