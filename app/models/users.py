# app/models/users.py
from category import Category
from recipe import Recipe


class User(object):
    ''' Creates and manipulates categories and recipes '''

    def __init__(self):
        self.categories = {}

    def create_category(self, category_name):
        ''' Creates the Category 
            Takes in one parameter, a string and creates an instance of the 
            class category and adds it to the categories dictionary

            :param category_name: A string: the name of the category to create
            :return: Categories dictionary, with the names as the keys and the 
            instance as the value
        '''
        if not isinstance(category_name, str):
            raise TypeError('Input should be a string')

        if category_name not in self.categories:
            new_category = Category(category_name)
            self.categories[category_name] = new_category
            return self.categories
        return ""

    def view_category(self, category_name):
        ''' Displays a Category
            Takes in one parameter, a string and checks the categories 
            dictionary for a key that matches the string.

            :param category_name: A string: the name of the category to view
            :return: The value of key that matches category name 
        '''
        return self.categories[category_name]

    def edit_category(self, category_name, new_category_name):
        ''' Takes in two parameters, 2 strings and checks the categories 
            dictionary for a key that matches the first string.Reassigns the 
            value to the 2nd string as the key, deletes the first strings pair.

            :param category_name: A string: the name of the category to edit
            :return: The dictionary categories
        '''
        if category_name in self.categories:
            self.categories[new_category_name] = self.categories[category_name]
            del self.categories[category_name]
            return self.categories

    def delete_category(self, category_name):
        ''' Takes in one parameter, checks the categories dictionary for a key 
            that matches the first string. Deletes the key value pair.

            :param category_name: A string: the name of the category to delete
            :return: The key and value pair that matches the category name 
        '''

        del self.categories[category_name]
        return self.categories

    def create_recipe(self, category_name, recipe_name):
        ''' Takes in two parameters, checks categories dictionary for key
            category_name. Creates a class instance recipe_name of class Recipe
            then appends the recipe_name to category_name's value, a list.

            :param category_name: A string: the name of the category
            :param recipe_name: A string: the name of the recipe
            :return: The key and value pair that matches the category_name
        '''
        the_category = self.categories[category_name]
        new_recipe = Recipe(recipe_name)
        the_category.recipes.append(new_recipe)

    def view_recipe(self, category_name, recipe_name):
        ''' Views a recipe '''
        the_recipes = self.categories[category_name].recipes

    def edit_recipe(self, category_name, recipe_name, new_recipe_name):
        ''' Edits a recipe '''
        pass

    def delete_recipe(self, category_name, recipe_name):
        ''' Deletes a recipe '''
        pass


new = User()
print(new.create_category("Cakes"))
print(new.create_category("chapati"))
print(new.view_category('chapati'))
