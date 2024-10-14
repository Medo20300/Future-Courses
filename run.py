
# Import the application creation function from the main package
from pythonic import create_app
# Import the Flask app object
from flask import app
# Create an instance of the Flask application
app = create_app()

# Run the application with debugging enabled and listening on port 5000
if __name__ == "__main__":
    app.run(debug=True, port=5000)
   
