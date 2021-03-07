import os
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config):

    if os.getenv('FLASK_CONFIG') == "production":
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
        )
    else:
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object('config')
        app.config.from_pyfile('config.py')


    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "admin.login"
    login_manager.login_message_category = "info"



    from repomas import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    from .student import student as student_blueprint
    app.register_blueprint(student_blueprint)

    from .medical import med as medical_blueprint
    app.register_blueprint(medical_blueprint)

    from .infoprod import info as info_blueprint
    app.register_blueprint(info_blueprint)


    return app
