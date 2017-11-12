# app/models/yummyApp.py
''' This script creates(signs up) and sign in users '''

# Local import
from app.models.users import User
from app.models.category import Category
from app.models.recipe import Recipe

# Third party imports
from werkzeug.security import check_password_hash


class YummyApp(object):
    ''' Signs up, signs in and signs out users '''

    def __init__(self):
        self.users = {}

    def signup(self, new_user):
        ''' Signs up new users.
            Takes an instance of the User class, checks if the username doesn't
            exist. It adds the user to the users dictionary.

            :param new_user: class instance:
        '''

        if isinstance(new_user, User):
            if new_user.username not in self.users:
                self.users[new_user.username] = new_user
                return True
            return False
        return 'User was not created'

    def signin(self, username, password):
        """Signs in existing users.
        Takes in 2 parameters. Check is the username exists in users.Checks if
        the entered password matches the credentials saved with the username

        :param username: A string:
        :param password:
        """

        # check if username exists
        if username in self.users:
            # check if password matches the value of the username key
            hash_pswd = self.users[username].hashed_pswd
            if check_password_hash(hash_pswd, password):
                # return that users instance
                return self.users[username]
            return "The username and password combination \
                        does not exist"
        return "The username does not exist, please signup"

    def create_category(self, username, category_name, description):
        ''' Creates the Category
            Takes in three parameters, 3 strings, checks if the username exists
            in the users dictionary. If user exists, creates an instance of the
            class category and adds it to the categories dictionary with the
            category name as the key and category name and description as
            attributes

            :param username: A string: the name of the active user
            :param category_name: A string: the name of the category to create
            :return: Categories dictionary, with the names as the keys and the
            instance as the value
        '''

        if username in self.users:
            if not all(isinstance(i, str) for i in [category_name,
                                                    description]):
                raise TypeError('Input should be a string')

            users_categories = self.users[username].categories
            if category_name not in users_categories:
                new_category = Category(category_name, description)
                users_categories[category_name] = new_category
                return users_categories
            return "A category by that name already exists"
        return 'Username does not exist'

    def view_category(self, username, category_name):
        ''' Displays a Category
            Takes in two parameters, 2 strings, checks if the username exists
            in the users dictionary. If user exists then checks the categories
            dictionary for a key that matches the string.

            :param username: A string: the name of the active user
            :param category_name: A string: the name of the category to view
            :return: The value of key that matches category name
        '''
        if username in self.users:
            return self.users[username].categories[category_name]
        return 'Username does not exist'

    def edit_category(self, username, category_name, description):
        ''' Editing a category
            Takes in three parameters, 3 strings, checks if the username exists
            in the users dictionary. If user exists, checks the categories
            dictionary for a key that matches the first string.Edits the
            details.

            :param username: A string: the name of the active user
            :param category_name: A string: the name of the category to edit
            :param description: A string: Some details on the category
            :return: The dictionary categories
        '''

        # updating just the description
        if username in self.users:
            if not all(isinstance(i, str) for i in [category_name,
                                                    description]):
                raise TypeError('Input should be a string')

            users_categories = self.users[username].categories
            updated_category = Category(category_name, description)
            users_categories[category_name] = updated_category
            ''' return users_categories '''

    def delete_category(self, username, category_name):
        ''' Deleting a category
            Takes in two parameters, 2 strings, checks if the username exists
            in the users dictionary. If user exists then checks the categories
            dictionary for a key that matches the first string.
            Deletes the key:value pair.

            :param username: A string: the name of the active user
            :param category_name: A string: the name of the category to delete
            :return: The remaining categories
        '''

        if username in self.users:
            if not isinstance(category_name, str):
                raise TypeError('Input should be a string')

            users_categories = self.users[username].categories
            del users_categories[category_name]
            return users_categories
        return 'Username does not exist'

    def create_recipe(self, username, category_name, recipe_name, ingredients):
        ''' Creates recipes in a specified category.
            Takes in three parameters, 3 strings, checks if the username exists
            in the users dictionary. If user exists,checks categories
            dictionary for key category_name. Creates a class instance
            recipe_name of class Recipe then appends the recipe_name to
            category_name's value, a list.

            :param username: A string: the name of the active user
            :param category_name: A string: the name of the category
            :param recipe_name: A string: the name of the recipe
            :return: The dictionary of recipes in the category instance
        '''

        if username in self.users:
            if not all(isinstance(i, str) for i in [category_name,
                                                    recipe_name, ingredients]):
                raise TypeError('Input should be a string')

            users_categories = self.users[username].categories
            the_category = users_categories[category_name]
            new_recipe = Recipe(recipe_name, ingredients)
            the_category.recipes[recipe_name] = new_recipe
            return the_category.recipes
        return 'Username does not exist'

    def view_recipes(self, username, category_name):
        """ Views all the recipes
            Takes in two parameters, 2 strings, checks if the username exists
            in the users dictionary. If user exists then checks the categories
            dictionary for a key that matches the first string and returns
            a list of the recipe dictionary values

            :param username: A string: the name of the active user
            :param category_name: A string:
            :return: A list of the recipe dictionary values
        """
        if username in self.users:

            users_categories = self.users[username].categories
            all_recipes = users_categories[category_name].recipes
            return all_recipes
        return 'Username does not exist'

    def view_recipe(self, username, category_name, recipe_name):
        ''' Views a recipe
            Takes in three parameters, 3 strings. Checks if the username exists
            in the users dictionary. If user exists, then checks the categories
            dictionary for a key that matches the first string. if it does. it 
            checks the recipe dictionary for a key that matches recipe_name and
            returns the category instance

            :param username: A string: the name of the active user
            :param category_name: A string: the name of the category
            :param recipe_name: A string: the name of the recipe
            :return: The instance of the recipe name key
        '''

        if username in self.users:
            users_categories = self.users[username].categories
            the_recipes = users_categories[category_name].recipes

            if recipe_name in the_recipes:
                return the_recipes[recipe_name].recipe_name
            return 'A recipe by that name was not found in the category'
        return 'Username does not exist'

    def edit_recipe(self, username, category_name, recipe_name, ingredients):
        ''' Edits a recipe
            Takes in three parameters, checks categories dictionary for key
            category_name. checks the recipes dictionary in the category for
            the recipe name. replaces it's description with a new one

            :param username: A string: the name of the active user
            :param category_name: A string: the name of the category
            :param recipe_name: A string: the name of the recipe
            :return: The dictionary of recipes
        '''
        if username in self.users:
            users_categories = self.users[username].categories
            the_recipes = users_categories[category_name].recipes
            updated_recipe = Recipe(recipe_name, ingredients)
            the_recipes[recipe_name] = updated_recipe

        return 'Username does not exist'

    def delete_recipe(self, username, category_name, recipe_name):
        ''' Deletes a recipe.
            Takes in three parameters, 3 strings. Checks if the username exists
            in the users dictionary. If user exists, then checks categories
            dictionary for keymcategory_name. checks the recipes dictionary in
            the category for the recipe name. deletes the recipe.

            :param username: A string: the name of the active user
            :param category_name: A string: the name of the category
            :param recipe_name: A string: the name of the recipe
            :return: The list in the category instance
        '''

        if username in self.users:
            if not isinstance(category_name, str):
                raise TypeError('Input should be a string')

            users_categories = self.users[username].categories
            del users_categories[category_name].recipes[recipe_name]
            return users_categories[category_name].recipes
        return 'Username does not exist'
