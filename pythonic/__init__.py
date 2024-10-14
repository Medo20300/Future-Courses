# Import necessary modules and extensions for the Flask application
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # For database interaction
from flask_bcrypt import Bcrypt  # For password hashing
from flask_login import LoginManager  # For user authentication management
from flask_migrate import Migrate  # For handling database migrations
from flask_ckeditor import CKEditor  # For integrating rich text editing
from flask_modals import Modal  # For handling modals in the app
from flask_mail import Mail  # For sending emails through the app
from pythonic.config import Config  # Application configuration settings
from flask_admin import Admin  # For integrating the Flask-Admin interface

# Initialize SQLAlchemy (database connection)
db = SQLAlchemy()

# Initialize other Flask extensions
bcrypt = Bcrypt()  # Initialize Bcrypt for password hashing
migrate = Migrate(db)  # Initialize Flask-Migrate for database migration handling
login_manager = LoginManager()  # Initialize Flask-Login for managing user sessions
ckeditor = CKEditor()  # Initialize CKEditor for rich text editing functionality
modal = Modal()  # Initialize Modal for handling modals in the app

# Configure the login manager to redirect to the login page and set flash message category
login_manager.login_view = "users.login"  # Redirect to login page for unauthorized users
login_manager.login_message_category = "info"  # Flash message category for login-related info

# Initialize Flask-Mail for email functionality
mail = Mail()


admin = Admin()

# Import models after defining db to avoid circular imports
from pythonic.models import db, Subscriber

# Define the create_app function to set up the Flask application
def create_app(config_calss=Config):
    # Create the Flask application instance
    app = Flask(__name__)
    
    # Load the configuration from the Config class
    app.config.from_object(Config)

    # Import custom admin index view from adminbp.routes
    from pythonic.adminbp.routes import MyAdminIndexView

    # Initialize all extensions with the Flask app instance
    db.init_app(app)  # Initialize SQLAlchemy with the app
    bcrypt.init_app(app)  # Initialize Bcrypt with the app
    login_manager.init_app(app)  # Initialize Flask-Login with the app
    ckeditor.init_app(app)  # Initialize CKEditor with the app
    modal.init_app(app)  # Initialize Modal with the app
    mail.init_app(app)  # Initialize Flask-Mail with the app
    admin.init_app(app, index_view=MyAdminIndexView())  # Initialize Flask-Admin with custom index view

    # Import blueprints for different parts of the app
    from pythonic.main.routes import main  # Main blueprint for main routes
    from pythonic.users.routes import users  # Users blueprint for user-related routes
    from pythonic.lessons.routes import lessons  # Lessons blueprint for lessons-related routes
    from pythonic.courses.routes import courses_bp  # Courses blueprint for courses-related routes
    from pythonic.errors.handlers import errors  # Errors blueprint for handling errors
    from pythonic.adminbp.routes import adminbp  # Admin blueprint for admin routes

    # Register all blueprints with the Flask app instance
    app.register_blueprint(adminbp)  # Register admin blueprint
    app.register_blueprint(main)  # Register main blueprint
    app.register_blueprint(users)  # Register users blueprint
    app.register_blueprint(lessons)  # Register lessons blueprint
    app.register_blueprint(courses_bp)  # Register courses blueprint
    app.register_blueprint(errors)  # Register errors blueprint
    
    # Return the created app instance
    return app
