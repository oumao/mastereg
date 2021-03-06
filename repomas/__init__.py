from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')


    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)


    from repomas import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    from .student import student as student_blueprint
    app.register_blueprint(student_blueprint)


    return app
