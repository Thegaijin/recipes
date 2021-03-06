# app.forms.py
''' This script has the forms for picking up the data '''

# Local imports
from app.models.yummyapp import YummyApp

# Third party imports
from flask import flash
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, PasswordField, ValidationError)
from wtforms.validators import DataRequired, EqualTo

my_user = YummyApp()


class RegisterForm(FlaskForm):
    ''' For creating user accounts '''

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                             DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Sign Up')

    def validate_username(self, field):
        """To check if the username entered already exists"""

        username = field.data
        if username in my_user.users:
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
        if username not in my_user.users:
            flash('Username does not exist.')
            raise ValidationError('Username does not exist.')
        return True


class CategoryForm(FlaskForm):
    """Form for creating categories"""

    name = StringField('Enter a Category name', validators=[DataRequired()])
    description = StringField(
        'Enter a Category Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RecipeForm(FlaskForm):
    """Form for creating categories"""

    name = StringField('Enter a Recipe name', validators=[DataRequired()])
    description = StringField(
        'Enter the Ingredients', validators=[DataRequired()])
    submit = SubmitField('Submit')
