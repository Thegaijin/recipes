# app/views.py

# Local imports
from app import app
from app import login_manager
from app.models.users import User
from app.models.yummyApp import YummyApp
from .forms import RegisterForm, LoginForm, CreateForm


# Third party imports
from flask import render_template
from flask import (flash, redirect, render_template, request, url_for)
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash


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
            # creating a user id
            if len(user.users) == 0:
                id = 1
            id = len(user.users) + 1

            # hashing the password
            pswd_hash = generate_password_hash(password)

            # creating instance of new_user
            new_user = User(id, username, pswd_hash)

        # add employee to the users dictionary and return True if done
        created = user.signup(new_user)
        flash('{}, Your account has been created'.format(username))

        if created:
            # redirect to the login page
            return redirect(url_for('signin'))
        flash("User account was not created")

    # load sign up template
    return render_template('home.html', form=form)


@app.route('/login', methods=["GET", "POST"])
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

            return redirect(url_for('categories'))

    # render the login template
    return render_template('login.html', form=form)


@app.route('/logout')
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


@app.route('/create_category',  methods=["GET", "POST"])
@login_required
def categories():
    '''Renders the functionality of the categories route

    :param category_name:
    '''

    create_category = True
    form = CreateForm()
    if form.validate_on_submit():
        category_name = form.name.data
        description = form.description.data

        if category_name not in user.users[current_user.username].categories:
            # creating a user id
            if len(user.users[current_user.username].categories) == 0:
                id = 1
            id = len(user.users[current_user.username].categories) + 1

        all_categories = user.users[current_user.username].create_category(
            id, category_name, description)
        the_categories = list(all_categories.values())
        return render_template('categories.html', form=form,
                               title="Categories", categories=the_categories)

    categories = user.users[current_user.username].categories
    the_categories = list(categories.values())
    return render_template('categories.html', form=form,
                           action='create_category',
                           title="Categories", categories=the_categories)


@app.route('/edit_category/<category_name>', methods=['GET', 'POST'])
@login_required
def edit_category(category_name):
    """Enables the functionality on the /edit_category route

    :param category_name:
    """
    create_category = False
    edit_category = True
    the_category = user.users[current_user.username].view_category(
        category_name)
    form = CreateForm(obj=the_category)
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data

        all_categories = user.users[current_user.username].edit_category(
            name, description)
        the_categories = list(all_categories.values())

        return render_template('categories.html', form=form,
                               title="Edit Category",
                               categories=the_categories)
    flash("Edit the {} category".format(category_name))
    return render_template('categories.html', form=form,
                           action='edit_category', title="Edit Category")


@app.route('/view_category/<category_name>', methods=['GET', 'POST'])
@login_required
def view_category(category_name):
    """Renders the recipes template to display recipes in the category

    :param category_name:
    """
    the_category = user.users[current_user.username].view_category(
        category_name)
    form = CreateForm()
    if form.validate_on_submit():
        name = form.name.data
        ingredients = form.description.data
        working_user = user.users[current_user.username]
        all_recipes = working_user.create_recipe(
            category_name, name, ingredients)
    all_recipes = the_category.recipes
    the_recipes = list(all_recipes.values())
    return render_template('ingredients.html', form=form, title="Recipes",
                           recipes=the_recipes, category=the_category)


@app.route('/delete_category/<category_name>', methods=['GET', 'POST'])
@login_required
def delete_category(category_name):
    """Enables the functionality on the delete_category route

    :param category_name:
    """
    form = CreateForm()
    all_categories = user.users[current_user.username].delete_category(
        category_name)
    the_categories = list(all_categories.values())

    return render_template('categories.html', title="Categories", form=form,
                           categories=the_categories)


''' @app.route('/create_recipe/<category_name>/<recipe_name>',
           methods=['GET', 'POST'])
@login_required
def create_recipe(category_name):
    create_recipe = True
    form = CreateForm()
    if form.validate_on_submit():
        category_name = form.name.data
        ingredients = form.description.data

    all_recipes = user.users[current_user.username].create_recipes(
        recipe_name, ingredients)
    the_recipes = list(all_recipes.values())
    return redirect(url_for'ingredients.html', form=form,
                           title="Recipes", recipes=the_recipes)

    recipes = user.users[current_user.username].categories[category_name].recipes
    the_recipes = list(recipes.values())
    return render_template('ingredients.html', form=form,
                           action='create_recipe',
                           title="Recipes", recipes=the_recipes) '''


@app.route('/delete_recipe/<category_name>/<recipe_name>',
           methods=['GET', 'POST'])
@login_required
def view_recipe(category_name, recipe_name):
    pass


@app.route('/delete_recipe/<category_name>/<recipe_name>',
           methods=['GET', 'POST'])
@login_required
def delete_recipe(category_name, recipe_name):
    """Enables the functionality on the delete_category route

    :param category_name: A string:
    :param recipe_name: A string:
    """
    form = CreateForm()
    all_recipes = user.users[current_user.username].delete_recipe(
        recipe_name)
    the_recipes = list(all_recipes.values())

    return render_template('ingredients.html', title="Ingredients", form=form,
                           recipes=the_recipes)
