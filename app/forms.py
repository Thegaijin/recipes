# app.forms.py

# Local imports
from app.models.recipe import Recipe
from app.models.users import User
from app.models.yummyApp import YummyApp

# Third party imports
from flask import flash
from flask_wtf import FlaskForm
from wtforms import (validators, StringField,
                     SubmitField, PasswordField, ValidationError)
from wtforms.validators import DataRequired, EqualTo

user = YummyApp()


class RegisterForm(FlaskForm):
    ''' For creating user accounts '''

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                             DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up')

    def validate_username(self, field):
        """To check if the username entered already exists"""

        username = field.data
        if username in user.users:
            flash('Username is already in use.')
            raise ValidationError('Username is already in use.')
        return True


class LoginForm(FlaskForm):
    """Form for users to log in"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

    def validate_usercredentials(self, field):
        """To checks if a username by that username exists"""

        username = field.data
        if username not in user.users:
            flash('Username does not exist.')
            raise ValidationError('Username does not exist.')
        return True
