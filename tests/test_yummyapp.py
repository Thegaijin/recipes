# app/tests/test_yummyapp.py
''' This script tests the functionality of yummy class '''

# third party imports
from unittest import TestCase

# local imports
from app.models.yummyapp import YummyApp
from app.models.users import User


class YummpyAppTestCase(TestCase):
    '''Testing the methods in the YummyApp class  '''

    def setUp(self):
        self.the_app = YummyApp()
        self.the_users = self.the_app.users
        self.the_user = User('username', 'password')
        self.new_user = User('username', 'password')

    def test_yummyapp_instance(self):
        ''' Test if an instance of YummyApp is created '''

        self.assertIsInstance(self.the_app, YummyApp,
                              msg='Object should be instance of YummyApp')

    def test_yummyapp_user_already_exists(self):
        ''' Test if a username is already taken '''

        self.the_app.signup(self.the_user)
        potential_user = self.the_app.signup(self.new_user)
        self.assertFalse(potential_user, msg='That username already exists')

    def test_yummyapp_user_sign_up(self):
        ''' Test if a user can sign up '''
        self.the_app.signup(self.the_user)
        self.assertIn(self.the_user.username, self.the_users,
                      msg='The user was not able to sign up')

    def test_yummyapp_user_sign_in(self):
        ''' Test if existing user can sign in if their credentials match '''

        self.the_app.signup(self.the_user)
        self.the_app.signin('username', 'password')
        self.assertEqual('password', self.the_users['username'].hashed_pswd,
                         msg='The username and password combination does not \
                        exist')

#######################################################################
#                            CATEGORY TESTS                           #
#######################################################################

    def test_yummyapp_category_creation(self):
        ''' Test if the category is created and added to the list '''

        self.the_app.signup(self.the_user)
        self.the_app.create_category('username', "cakes", 'baked goods')
        self.assertIn('cakes', self.the_users['username'].categories,
                      msg='The category was not added')

    def test_yummyapp_category_view(self):
        ''' Test if the category can be viewed '''

        self.the_app.signup(self.the_user)
        self.the_app.create_category('username', "cakes", 'baked goods')
        viewed = self.the_app.view_category('username', "cakes")
        self.assertEqual('cakes', viewed.category_name,
                         msg='A category by that name doesn\'t exist')

    def test_yummyapp_category_name_edit(self):
        ''' Test if the category name can be edited '''

        self.the_app.signup(self.the_user)
        self.the_app.create_category('username', "cakes", 'baked goods')
        self.the_app.edit_category('username', "Bun", 'bun on a bun')
        self.assertIn('Bun', self.the_users['username'].categories,
                      msg='The category wasn\'t edited')

    def test_yummyapp_category_edit(self):
        ''' Test if the category can be edited '''

        self.the_app.signup(self.the_user)
        self.the_app.create_category('username', "cakes", 'baked goods')
        self.the_app.edit_category('username', "cakes", 'dough on dough')
        categories = self.the_users['username'].categories
        self.assertEqual('dough on dough', categories['cakes'].description,
                         msg='The category description wasn\'t edited')

    def test_yummyapp_category_deletion(self):
        ''' Test if categories can be deleted '''
        self.the_app.signup(self.the_user)
        self.the_app.create_category('username', "cakes", 'baked goods')
        self.the_app.delete_category('username', "cakes")
        self.assertNotIn('cakes', self.the_users['username'].categories,
                         msg='The category was not deleted')

#######################################################################
#                              RECIPE TESTS                           #
#######################################################################

    def test_yummyapp_recipe_is_created(self):
        ''' Test if the recipe is created and added to the dictionary '''

        self.the_app.signup(self.the_user)
        self.the_app.create_category('username', 'Cakes', 'baked goods')
        self.the_app.create_recipe(
            'username', 'Cakes', 'cupcakes', 'cakes in a cup')
        categories = self.the_users['username'].categories
        self.assertIn('cupcakes', categories['Cakes'].recipes)

    def test_yummyapp_if_recipe_is_viewed(self):
        ''' Test if the recipe can be viewed '''

        self.the_app.signup(self.the_user)
        self.the_app.create_category('username', 'Cakes', 'baked goods')
        self.the_app.create_recipe(
            'username', 'Cakes', 'cupcakes', 'cakes in a cup')
        viewed_recipe = self.the_app.view_recipe(
            'username', 'Cakes', 'cupcakes')
        self.assertEqual(
            'cupcakes', viewed_recipe)

    def test_yummyapp_recipes_are_viewed(self):
        ''' Test if all the recipes can be viewed '''

        self.the_app.signup(self.the_user)
        self.the_app.create_category('username', 'Cakes', 'baked goods')
        self.the_app.create_recipe(
            'username', 'Cakes', 'cupcakes', 'cakes in a cup')
        self.the_app.create_recipe('username', 'Cakes', 'buns', 'bun bun')
        viewed_recipes = self.the_app.view_recipes('username', 'Cakes')
        result_len = len(viewed_recipes)
        self.assertEqual(2, result_len)

    def test_yummyapp_recipe_can_edit_recipe(self):
        ''' Test if the recipe can be edited '''

        self.the_app.signup(self.the_user)
        self.the_app.create_category('username', 'Cakes', 'baked goods')
        self.the_app.create_recipe(
            'username', 'Cakes', 'cupcakes', 'cakes in a cup')
        self.the_app.edit_recipe(
            'username', 'Cakes', 'cupcakes', 'dough on dough')
        categories = self.the_users['username'].categories
        self.assertEqual(
            'dough on dough',
            categories['Cakes'].recipes['cupcakes'].ingredients)

    def test_yummyapp_can_delete_recipe(self):
        ''' Test if a recipe can be deleted from a category '''

        self.the_app.signup(self.the_user)
        self.the_app.create_category('username', 'Cakes', 'baked goods')
        self.the_app.create_recipe(
            'username', 'Cakes', 'cupcakes', 'cakes in a cup')
        self.the_app.delete_recipe('username', 'Cakes', 'cupcakes')
        categories = self.the_users['username'].categories
        self.assertNotIn('cupcakes', categories['Cakes'].recipes)
