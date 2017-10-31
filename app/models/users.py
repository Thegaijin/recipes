# app/models/users.py


class User(object):
    ''' Creates and manipulates categories and recipes '''

    def __init__(self):
        self.categories = {}

    def create_category(self, name):
        ''' Creates the Category 
        :param: name
        '''
        pass

    def view_category(self, name):
        ''' Displays a Category '''
        pass

    def edit_category(self, name, newname):
        ''' Edits a Category '''
        pass

    def delete_category(self, name):
        ''' Deletes a Category '''
        pass

    def create_recipe(self, name):
        ''' Creates a recipe '''
        pass

    def view_recipe(self, name):
        ''' Creates a recipe '''
        pass

    def edit_recipe(self, name, newname):
        ''' Creates a recipe '''
        pass

    def delete_recipe(self, name):
        ''' Creates a recipe '''
        pass
