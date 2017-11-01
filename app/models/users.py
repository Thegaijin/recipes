# app/models/users.py


class User(object):
    ''' Creates and manipulates categories and recipes '''

    def __init__(self):
        self.categories = {}

    def create_category(self, category_name):
        ''' Creates the Category 
            :param category_name: A string: the name of the category to create
            :return: The dictionary of categories, with the names as the keys 
            and an empty list as the values
        '''
        if not isinstance(category_name, str):
            raise TypeError('Input should be a string')

        if category_name not in self.categories:
            self.categories[category_name] = []
            return self.categories
        return ""

    def view_category(self, category_name):
        ''' Displays a Category '''
        viewed = {k: v for k, v in self.categories.items()
                  if category_name in k}
        pass

    def edit_category(self, category_name, newname):
        ''' Edits a Category '''
        pass

    def delete_category(self, category_name):
        ''' Deletes a Category '''
        pass

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
