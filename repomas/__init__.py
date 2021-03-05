from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(config):
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object[config]
    app.config.from_pyfile(config.py)


    db.init_app(app)

# @app.route('/')
# def home():
#     return render_template("home.html", title="Home")


# app.run(debug=True)
