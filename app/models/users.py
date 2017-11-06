# app/models/users.py

# Local imports
from app.models.category import Category
from app.models.recipe import Recipe

# Third party imports
from flask_login import UserMixin


class User(UserMixin):
    ''' Creates and manipulates categories and recipes '''

    def __init__(self, id, username, hashed_pswd):
        self.id = id
        self.username = username
        self.hashed_pswd = hashed_pswd
        self.categories = {}

    def get_id(self):
        """Overriding the id parameter to be username"""

        return self.username

    def create_category(self, category_name, description):
        ''' Creates the Category 
            Takes in one parameter, a string and creates an instance of the 
            class category and adds it to the categories dictionary
            :param category_name: A string: the name of the category to create
            :return: Categories dictionary, with the names as the keys and the 
            instance as the value
        '''

        if not isinstance(category_name, str):
            raise TypeError('Input should be a string')

        if description not in self.categories:
            new_category = Category(category_name, description)
            self.categories[category_name] = new_category
            return self.categories
        return "A category by that name already exists"

    def view_category(self, category_name):
        ''' Displays a Category
            Takes in one parameter, a string and checks the categories 
            dictionary for a key that matches the string.
            :param category_name: A string: the name of the category to view
            :return: The value of key that matches category name 
        '''
        return self.categories[category_name]

    def edit_category(self, category_name, description='None'):
        ''' Editing a category
            Takes in two parameters, 2 strings and checks the categories 
            dictionary for a key that matches the first string.Edits the 
            details.
            :param category_name: A string: the name of the category to edit
            :param description: A string: Some details on the category
            :return: The dictionary categories
        '''
        if description is None:
            description = 'N/A'
        updated_category = Category(category_name, description)
        self.categories[category_name] = updated_category
        return self.categories

    def delete_category(self, category_name):
        ''' Deleting a category
            Takes in one parameter, checks the categories dictionary for a key 
            that matches the first string. Deletes the key value pair.
            :param category_name: A string: the name of the category to delete
            :return: The remaining categories
        '''

        del self.categories[category_name]
        return self.categories

    def create_recipe(self, category_name, recipe_name, ingredients):
        ''' Creates recipes in a specified category.
            Takes in two parameters, checks categories dictionary for key
            category_name. Creates a class instance recipe_name of class Recipe
            then appends the recipe_name to category_name's value, a list.
            :param category_name: A string: the name of the category
            :param recipe_name: A string: the name of the recipe
            :return: The dictionary of recipes in the category instance
        '''
        the_category = self.categories[category_name]
        new_recipe = Recipe(recipe_name, ingredients)
        the_category.recipes[recipe_name] = new_recipe
        return the_category.recipes

    def view_recipes(self, category_name):
        """ Views all the recipes
        Takes in one parameter, category_name and returns a list of the recipe 
        dictionary values
        :param category_name: A string:
        :return: A list of the recipe dictionary values
        """
        all_recipes = self.categories[category_name].recipes
        the_recipes = list(all_recipes.values())
        return the_recipes

    def view_recipe(self, category_name, recipe_name):
        ''' Views a recipe 
            Takes in two parameters, checks categories dictionary for key
            category_name. checks the recipes list in the category for the 
            recipe name
            :param category_name: A string: the name of the category
            :param recipe_name: A string: the name of the recipe
            :return: The list in the category instance
        '''
        the_recipes = self.categories[category_name].recipes
        print(the_recipes)
        ''' recipe_names = [recipe.recipe_name for recipe in the_recipes]
        if recipe_name in recipe_names: '''
        ''' return recipe_name '''
        if recipe_name in the_recipes:
            return the_recipes[recipe_name].recipe_name
        return 'A recipe by that name was not found in the category'

    def edit_recipe(self, category_name, recipe_name, ingredients='None'):
        ''' Edits a recipe
            Takes in two parameters, checks categories dictionary for key
            category_name. checks the recipes list in the category for the 
            recipe name. replaces it's description with a new one.abs

            :param category_name: A string: the name of the category
            :param recipe_name: A string: the name of the recipe
            :return: The dictionary of recipes
         '''

        the_recipes = self.categories[category_name].recipes
        if recipe_name in the_recipes:
            if ingredients is None:
                ingredients = 'Please enter some Ingredients for the recipe'
            updated_recipe = Recipe(recipe_name, ingredients)
            the_recipes[recipe_name] = updated_recipe
            return the_recipes
        return 'The recipe doesn\'t exist'

    def delete_recipe(self, category_name, recipe_name):
        ''' Deletes a recipe. 
            Takes in two parameters, checks categories dictionary for key
            category_name. checks the recipes list in the category for the 
            recipe name. deletes the recipe.

            :param category_name: A string: the name of the category
            :param recipe_name: A string: the name of the recipe
            :return: The list in the category instance
        '''

        del self.categories[category_name].recipes[recipe_name]
        return self.categories[category_name].recipes
