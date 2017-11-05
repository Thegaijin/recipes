[![Build Status](https://travis-ci.org/Thegaijin/recipes.svg?branch=flask-v1.2)](https://travis-ci.org/Thegaijin/recipes)

# Recipes
This application allows users to register an account and login to create, save and share recipes.

## Features

The application has the following features:

* A user can signup for an account in the app 
* A user can  signin into the app with their credentials
* A user can create, edit, share and delete categories and or recipes

## Setup

To use the application, ensure that you have python 3.6+, clone the repository to your local machine. Open your git commandline and run

    git clone https://github.com/Thegaijin/recipes.git

Enter the project directory

    cd recipes

Create a virtual environment

    virtualenv venv

Activate the virtual environment

    source venv/bin/activate

Then install all the required dependencies

    pip install -r requirements.txt

To start the application run:

    set FLASK_CONFIG=development
    set FLASK_APP=run.py
    flask run
