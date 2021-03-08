from flask import render_template
from . import home


@home.route('/')
def home():
    return render_template('home.html')