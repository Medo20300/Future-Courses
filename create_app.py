# Import the database instance from the models module
from pythonic.models import db


from pythonic import create_app
# Create an instance of the Flask application
app = create_app()
# Establish the application context and create the database schema
with app.app_context():
        db.create_all()

        # Print confirmation message once the database is created successfully
        print('Database created successfully')
