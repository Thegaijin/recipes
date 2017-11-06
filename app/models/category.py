# app/models/category.py


class Category(object):
    ''' The Category class is for creating category objects to hold
    the properties of a category  '''

    def __init__(self, category_name, description):
        self.category_name = category_name
        self.description = description
        self.recipes = {}
