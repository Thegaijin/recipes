# app/views.py
''' This script links the models to the templates '''

# Local imports
from app import app
from app import login_manager
from app.models.users import User
from app.models.yummyapp import YummyApp
from .forms import RegisterForm, LoginForm, CategoryForm, RecipeForm


# Third party imports
from flask import (flash, redirect, render_template, url_for)
from flask_login import login_required, login_user, logout_user, current_user
import re                               # handle non-alpahabetic characters
from werkzeug.security import generate_password_hash


user = YummyApp()


@app.route('/', methods=["GET", "POST"])
def register():
    """Handle requests to the /signup route
    Create a new user through the sign up form
    """
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username not in user.users:

            # hashing the password
            hashed_pswd = generate_password_hash(password)

            # creating instance of new_user
            new_user = User(username, hashed_pswd)

        # add employee to the users dictionary and return True if done
        created = user.signup(new_user)
        flash('{}, Your account has been created'.format(username))

        if created:
            # redirect to the login page
            return redirect(url_for('signin'))
        flash("User account was not created")

    # load sign up template
    return render_template('home.html', form=form)


@app.route('/login/', methods=["GET", "POST"])
def signin():
    """Handle requests to the /home route
    Log a user in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # return instance of current user
        loggedin = user.signin(username, password)
        flash("Welcome, {}".format(loggedin.username))
        if isinstance(loggedin, User):
            login_user(loggedin)

            return redirect(url_for('create_category'))

    # render the login template
    return render_template('login.html', form=form)


@app.route('/logout/')
@login_required
def logout():
    """Handle requests to the /logout route

    Log users out of the app
    """
    logout_user()
    flash('You have successfully been logged out.')
    # redirect to the login page
    return redirect(url_for('signin'))


@login_manager.user_loader
def load_user(username):
    """Loads user from the users dictionary

    :param username:
    """

    return user.users.get(username)


@app.route('/create_category/', methods=["GET", "POST"])
@login_required
def create_category():
    '''Renders the functionality of the categories route
    :param category_name:
    '''

    form = CategoryForm()
    if form.validate_on_submit():
        category_name = form.name.data
        description = form.description.data

        # change name and description to lowercase
        category_name = category_name.lower()
        description = description.lower()
        present_categories = user.users[current_user.username].categories

        if category_name in present_categories:
            # Check if category name already exists

            error = 'A category by that name already exists'
            the_categories = list(present_categories.values())

            # clear the form
            form.name.data = ''
            form.description.data = ''
            return render_template('categories.html', form=form,
                                   categories=the_categories,
                                   button='Create Category', error=error)

        user.create_category(current_user.username,
                             category_name, description)
        # clear the form
        form.name.data = ''
        form.description.data = ''
        the_categories = list(present_categories.values())
        return render_template('categories.html', form=form,
                               title="Categories", categories=the_categories,
                               button='Create Category')

    categories = user.users[current_user.username].categories
    the_categories = list(categories.values())
    form = CategoryForm()
    return render_template('categories.html', form=form,
                           categories=the_categories, button='Create Category')


@app.route('/edit_category/<path:category_name>/', methods=['GET', 'POST'])
@login_required
def edit_category(category_name):
    """Enables the functionality on the /edit_category route

    :param category_name:
    """

    all_categories = user.users[current_user.username].categories
    the_category = user.view_category(current_user.username, category_name)

    form = CategoryForm(obj=the_category)
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data

        # change name and description to lowercase
        name = name.lower()
        description = description.lower()

        if name not in all_categories:
            current_categories = user.users[current_user.username].categories
            del current_categories[category_name]
            user.create_category(current_user.username,
                                 name, description)
            the_categories = list(all_categories.values())
            return redirect(url_for('create_category'))

        else:
            user.edit_category(current_user.username,
                               category_name, description)

            return redirect(url_for('create_category'))

    flash("Edit the {} category".format(category_name))
    return render_template('categories.html', form=form, title="Categories",
                           button='Edit Category')


@app.route('/view_category/<path:category_name>/', methods=['GET', 'POST'])
@login_required
def view_category(category_name):
    """Renders the recipes template to display recipes in the category

    :param category_name:
    """
    the_category = user.view_category(current_user.username, category_name)

    form = RecipeForm()
    if form.validate_on_submit():
        name = form.name.data
        ingredients = form.description.data

        # change name and ingredients to lowercase
        name = name.lower()
        ingredients = ingredients.lower()

        all_recipes = user.create_recipe(current_user.username,
                                         category_name, name, ingredients)
    all_recipes = the_category.recipes
    the_recipes = list(all_recipes.values())
    # clear the form
    form.name.data = ''
    form.description.data = ''
    return render_template('ingredients.html', form=form, title="Recipes",
                           recipes=the_recipes, category_name=category_name,
                           button='Create Recipe')


@app.route('/delete_category/<path:category_name>/', methods=['GET', 'POST'])
@login_required
def delete_category(category_name):
    """Enables the functionality on the delete_category route

    :param category_name:
    """
    form = CategoryForm()
    all_categories = user.delete_category(current_user.username, category_name)
    return redirect(url_for('create_category', form=form))


@app.route('/edit_recipe/<path:category_name>/<path:recipe_name>/',
           methods=['GET', 'POST'])
@login_required
def edit_recipe(category_name, recipe_name):
    """Renders the recipe template to edit recipes in the category

    :param category_name: A string:
    :param recipe_name: A string:
    """
    all_recipes = user.view_recipes(current_user.username,
                                    category_name)
    the_recipe = user.view_recipe(current_user.username,
                                  category_name, recipe_name)

    form = RecipeForm(obj=the_recipe)

    if form.validate_on_submit():
        name = form.name.data
        ingredients = form.description.data

        # change name and ingredients to lowercase
        name = name.lower()
        ingredients = ingredients.lower()

        if name not in all_recipes:
            del all_recipes[recipe_name]
            the_recipes = user.create_recipe(current_user.username,
                                             category_name, name, ingredients)
            my_recipes = list(the_recipes.values())
            form.name.data = ''
            form.description.data = ''
            return redirect(url_for('view_category',
                                    category_name=category_name))
        else:
            user.edit_recipe(current_user.username,
                             category_name, name, ingredients)

            return render_template('ingredients.html', form=form,
                                   title='Ingredients',
                                   category_name=category_name,
                                   recipes=the_recipes)
    flash("Edit the {} recipe in the {} category".format(
        recipe_name, category_name))
    return render_template('ingredients.html', form=form,
                           title='Ingredients',
                           category_name=category_name, button='Edit recipe')


@app.route('/delete_recipe/<path:category_name>/<path:recipe_name>/',
           methods=['GET', 'POST'])
@login_required
def delete_recipe(category_name, recipe_name):
    """Enables the functionality on the delete_category route

    :param category_name: A string:
    :param recipe_name: A string:
    """
    all_recipes = user.delete_recipe(current_user.username, category_name,
                                     recipe_name)
    the_recipes = list(all_recipes.values())
    form = RecipeForm()
    return redirect(url_for('view_category', category_name=category_name))
