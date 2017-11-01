# app/models/users.py


class User(object):
    ''' Creates and manipulates categories and recipes '''

    def __init__(self):
        self.categories = {}

    def create_category(self, category_name):
        ''' Creates the Category 
            Takes in one parameter, a string and adds it as a key to a 
            dictionary with a value of an empty list to hold recipes

            :param category_name: A string: the name of the category to create
            :return: Categories dictionary, with the names as the keys and an 
            empty list as the values
        '''
        if not isinstance(category_name, str):
            raise TypeError('Input should be a string')

        if category_name not in self.categories:
            self.categories[category_name] = []
            return self.categories
        return ""

    def view_category(self, category_name):
        ''' Displays a Category
            Takes in one parameter, a string and checks the categories 
            dictionary for a key that matches the string.

            :param category_name: A string: the name of the category to view
            :return: The key and value pair that matches the category name 
        '''
        viewed = {k: v for k, v in self.categories.items()
                  if category_name in k}
        return viewed

    def edit_category(self, category_name, new_category_name):
        ''' Takes in two parameters, 2 strings and checks the categories 
            dictionary for a key that matches the first string.Reassigns the 
            value to the 2nd string as the key, deletes the first strings pair.

            :param category_name: A string: the name of the category to view
            :return: The key and value pair that matches the category name 
        '''
        if category_name in self.categories:
            self.categories[new_category_name] = self.categories[category_name]
            del self.categories[category_name]
            return self.categories

    def delete_category(self, category_name):
        ''' Takes in one parameter, checks the categories dictionary for a key 
            that matches the first string. Deletes the key value pair.

            :param category_name: A string: the name of the category to view
            :return: The key and value pair that matches the category name 
        '''
        if category_name in self.categories:
            del self.categories[category_name]
            return self.categories

    def create_recipe(self, category_name, recipe_name):
        ''' Creates a recipe '''
        pass

    def view_recipe(self, category_name, recipe_name):
        ''' Creates a recipe '''
        pass

    def edit_recipe(self, category_name, recipe_name, new_recipe_name):
        ''' Creates a recipe '''
        pass

    def delete_recipe(self, category_name, recipe_name):
        ''' Creates a recipe '''
        pass


new = User()
print(new.create_category("Cakes"))
print(new.create_category("chapati"))
print(new.view_category('chapati'))
