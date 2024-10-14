import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flask_modals import Modal
from flask_mail import Mail
from pythonic.config import Config
from flask_admin import Admin

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate(db)
login_manager = LoginManager()
ckeditor = CKEditor()
modal = Modal()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
mail = Mail()
admin = Admin()


def create_app(config_calss=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    from pythonic.adminbp.routes import MyAdminIndexView
    # Initialize the SQLAlchemy database with the Flask app
    db.init_app(app)
    # Initialize Bcrypt for password hashing with the Flask app
    bcrypt.init_app(app)
    # Initialize the LoginManager for managing user sessions with the Flask app
    login_manager.init_app(app)
    # Initialize CKEditor for rich text editing functionality with the Flask app
    ckeditor.init_app(app)
    # Initialize Flask Modals for handling modal dialogs with the Flask app
    modal.init_app(app)
    # Initialize Flask-Mail for sending emails with the Flask app
    mail.init_app(app)
    # Initialize Flask-Admin with the app and set the custom admin index view
    admin.init_app(app, index_view=MyAdminIndexView())

    from pythonic.main.routes import main
    from pythonic.users.routes import users
    from pythonic.lessons.routes import lessons
    from pythonic.courses.routes import courses_bp
    from pythonic.errors.handlers import errors
    from pythonic.adminbp.routes import adminbp

    app.register_blueprint(adminbp)
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(lessons)
    app.register_blueprint(courses_bp)
    app.register_blueprint(errors)
    return app
