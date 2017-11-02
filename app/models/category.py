# app/models/category.py


class Category(object):
    ''' The Category class is for creating category objects to hold
    the properties of a category  '''

    def __init__(self, id, category_name):
        self.id = id
        self.category_name = category_name
        self.recipes = {}
