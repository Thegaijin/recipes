# app/views.py

# Local imports
from app import app
from app import login_manager
from app.models.users import User
from app.models.yummyApp import YummyApp
from .forms import RegisterForm, LoginForm


# Third party imports
from flask import render_template
from flask import (flash, redirect, render_template, request, session, url_for)
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash


''' @app.route('/')
def index():
    register_form = RegisterForm()
    login_form = LoginForm()
    return render_template('home.html', register_form=register_form,
                           login_form=login_form) '''
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
            flash("Now inside if statement")
            login_user(loggedin)
            flash("After login user")
            return redirect(url_for('categories'))

    # render the login template
    return render_template('login.html', form=form)


@login_manager.user_loader
def load_user(username):
    """Loads user from the users dictionary"""
    flash("In user loader")
    return user.users.get(username)


@app.route('/categories')
def categories():
    return render_template('categories.html')


@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html')
