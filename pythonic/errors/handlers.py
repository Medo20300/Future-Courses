# Importing Blueprint to organize error handling routes
from flask import Blueprint, render_template

# Creating a Blueprint named 'errors' to handle custom error pages.
errors = Blueprint('errors', __name__)


# This decorator registers a handler for the 404 error (Page Not Found).
@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

# Registers a handler for the 403 error (Forbidden).
@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403

# Registers a handler for the 500 error (Internal Server Error).
@errors.app_errorhandler(500)
def error_500(error):
    # Renders a custom '500.html' template and returns the 500 status code.
    return render_template('errors/500.html'), 500