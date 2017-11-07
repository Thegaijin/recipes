# app/tests/test_users.py

# third party imports
from unittest import TestCase

# local imports
from app.models.users import User
from app.models.category import Category

#######################################################################
#                            CATEGORY TESTS                           #
#######################################################################

######################## REFACTOR TO UNITTEST  ########################


class UserTestCase(TestCase):
    ''' Testing the functionality of the methods in the User Class '''

    def setUp(self):
        self.the_user = User( 'username', 'password')
        self.categories = self.the_user.categories

    def test_user_is_instance(self):
        """Test if instance of User class is successfully created"""

        # assert isinstance(new_user, User) is True
        self.assertIsInstance(self.the_user, User,
                              msg='Object should be instance of User class')

    ''' def test_user_if_category_doesnt_already_exist(self):
        Test if the category to be created doesn\'t already exist
        # FIXME: test gives assertion error
        self.the_user.create_category(1, "cakes", 'dough on dough on dough')
        self.assertNotIn("cakes", self.the_user.categories) '''

    def test_user_if_category_can_be_created(self):
        ''' Test if the category is created and added to the list '''

        self.the_user.create_category("cakes", 'baked goods')
        self.assertIn('cakes', self.the_user.categories,
                      msg='The category was not added')

    def test_user_if_category_can_be_viewed(self):
        ''' Test if the category can be viewed '''

        self.the_user.create_category("cakes", 'baked goods')
        viewed = self.the_user.view_category("cakes")
        self.assertEqual('cakes', viewed.category_name,
                         msg='A category by that name doesn\'t exist')

    def test_user_if_category_can_be_edited(self):
        ''' Test if the category can be edited '''

        self.the_user.create_category("cakes", 'baked goods')
        edited = self.the_user.edit_category("cakes", 'dough on dough')
        self.assertEqual('dough on dough',
                         self.categories['cakes'].description,
                         msg='The category description wasn\'t edited')

    def test__user_if_category_can_be_deleted(self):
        ''' Test if categories can be deleted '''

        self.the_user.create_category("cakes", 'baked goods')
        deleted = self.the_user.delete_category("cakes")
        self.assertNotIn('cakes', self.categories,
                         msg='The category was not deleted')

#######################################################################
#                              RECIPE TESTS                           #
#######################################################################

    def test_if_users_recipe_is_created(self):
        ''' Test if the recipe is created and added to the list '''

        ''' pre_length = len(new_user.categories['cakes'])
        new_user.create_recipe('cakes', 'cupcake')
        post_length = len(new_user.categories['cakes'])
        x = post_length - pre_length
        assert x == 1
        assert 'cupcakes' in new_user.categories['cakes'] '''
        self.the_user.create_category('Cakes', 'baked goods')
        self.the_user.create_recipe(
            'Cakes', 'cupcakes', 'cakes in a cup')
        self.assertIn('cupcakes', self.categories['Cakes'].recipes)

    def test_users_if_recipe_is_viewed(self):
        ''' Test if the recipe can be viewed '''

        self.the_user.create_category('Cakes', 'baked goods')
        self.the_user.create_recipe('Cakes', 'cupcakes', 'cakes in a cup')
        viewed_recipe = self.the_user.view_recipe('Cakes', 'cupcakes')
        self.assertEqual(
            'cupcakes', viewed_recipe)

    def test_usersif_recipe_can_be_edited(self):
        ''' Test if the recipe can be edited '''

        self.the_user.create_category('Cakes', 'baked goods')
        self.the_user.create_recipe('Cakes', 'cupcakes', 'cakes in a cup')
        self.the_user.edit_recipe('Cakes', 'cupcakes', 'dough on dough')
        self.assertEqual(
            'dough on dough',
            self.categories['Cakes'].recipes['cupcakes'].ingredients)

    def test_user_can_delete_recipe(self):
        ''' Test if a recipe can be deleted from a category  '''

        self.the_user.create_category('Cakes', 'baked goods')
        self.the_user.create_recipe('Cakes', 'cupcakes', 'cakes in a cup')
        self.the_user.delete_recipe('Cakes', 'cupcakes')
        self.assertNotIn('cupcakes', self.categories['Cakes'].recipes)
