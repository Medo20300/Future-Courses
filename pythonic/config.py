
import os
class Config:
    # Secret key for session management and security
    SECRET_KEY = os.environ.get('SECRET_KEY', '6029178fffcca61d16f1bb363270419710da3f535d8353c972c91b4f59909cd7')  # Set a default key for development

    # Database configuration using MySQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI', 
        'mysql+pymysql://root:hellomysql@localhost/learning'  # Fixed the formatting here
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