# app/models/recipe.py


class Recipe(object):
    ''' Hold the details for categories '''

    def __init__(self, recipe_name):
        self.recipe_name = recipe_name
        self.ingredients = {}