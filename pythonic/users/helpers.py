from pythonic import mail
from flask_mail import Message # Import Flask-Mail's Message class to send emails
from flask import url_for


def send_reset_email(user):
    """Function to send a password reset email to the user"""

    token = user.get_reset_token() # Generate a password reset token for the user
    msg = Message(
        "Pythonic App Password Reset Request",
        sender="ElearnApp.project@gmail.com",
        recipients=[user.email],  # The recipient's email address
        body=f"""To reset your password, visit the following link:
        {url_for('users.reset_password', token=token, _external=True)}
        
        if you did not make this request, please ignore this email.""",
    )
    mail.send(msg)  # Send the email using Flask-Mail's `send` function
