# app/models/recipe.py


class Recipe(object):
    ''' The Recipe class is for creating recipe objects to hold
    the properties of a recipe 
    '''

    def __init__(self, recipe_name, ingredients):
        self.recipe_name = recipe_name
        self.ingredients = ingredients
