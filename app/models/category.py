# app/models/category.py


class Category(object):
    ''' Hold the details for categories '''

    def __init__(self, category_name):
        self.category_name = category_name
        self.recipes = {}