
# The Config class defines the configuration settings for the Flask application, including security, database, email, and CKEditor settings.

# The SECRET_KEY is used for session management and security purposes. It is fetched from an environment variable, but a default key is provided for development use.

# The SQLALCHEMY_DATABASE_URI sets up the connection to the MySQL database using SQLAlchemy. It also defaults to a local MySQL database configuration for development if no environment variable is provided.
# SQLALCHEMY_TRACK_MODIFICATIONS is set to False to disable the modification tracking system, improving resource usage by avoiding unnecessary overhead.

# CKEditor settings are included to enable the use of code snippets in the editor and specify a file upload handler route.

# The MAIL_SERVER, MAIL_PORT, and MAIL_USE_TLS are configured for email functionality using Gmail's SMTP server, with TLS enabled for secure communication.
# The email credentials (MAIL_USERNAME and MAIL_PASSWORD) are pulled from environment variables to ensure security in production, but default values are provided for development.

# This configuration is designed to be flexible, allowing for easy adjustments between development and production environments by simply setting environment variables.

import os
class Config:
    # Secret key for session management and security
    SECRET_KEY = os.environ.get('SECRET_KEY', '6029178fffcca61d16f1bb363270419710da3f535d8353c972c91b4f59909cd7')  # Set a default key for development

    # Database configuration using MySQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI', 
        'mysql+pymysql://root:PASSword!!123@localhost/learning'  # Fixed the formatting here
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable track modifications to save resources

    # CKEditor configurations
    CKEDITOR_ENABLE_CODESNIPPET = True  # Enable code snippets in CKEditor
    CKEDITOR_FILE_UPLOADER = "main.upload"  # Define file upload handler
    
    # Email server configuration for sending emails
    MAIL_SERVER = "smtp.gmail.com"   # Gmail SMTP server
    MAIL_PORT = 587  # Port for TLS
    MAIL_USE_TLS = True  # Use TLS
    MAIL_USERNAME = os.environ.get("EMAIL_USER", 'ElearnApp.project@gmail.com')  # Set default email for development
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS", 'ypgkyyfwlommkykyr')  # Set default email password for development
