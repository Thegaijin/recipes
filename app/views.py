# app/views.py

# Local imports
from app import app
# Third party imports
from flask import render_template


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/categories')
def categories():
    return render_template('categories.html')


@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html')
