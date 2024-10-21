from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from pythonic.models import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Regexp,
    EqualTo,
    ValidationError,
)


class RegistrationForm(FlaskForm):
    """Registration form for new users"""

    fname = StringField(
        "First Name", validators=[DataRequired(), Length(min=2, max=25)]
    )
    lname = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=25)])
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=25)]
    )
    permission = SelectField(
        'Permission', choices=[('student', 'Student'), ('mentor', 'Mentor')]  # Dropdown to select user role (student or mentor)
    ) 

    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            # Password must meet complexity requirements: 1 lowercase, 1 uppercase, 1 number, 1 special character, 8-32 characters
            Regexp(
                r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#_])[A-Za-z\d@$!%*?&#_]{8,32}$"
            ),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        """Validator to check if the username already exists in the database"""

        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                "Username already exists! Please choses a different one"
            )

    def validate_email(self, email):
        """Validator to check if the email already exists in the database"""

        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already exists! Please choses a different one")


class LoginForm(FlaskForm):
    """Login form for existing users"""

    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),  # Field for password with validation
        ],
    )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")


class UpdateProfileForm(FlaskForm):
    """Form to update user profile"""

    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=25)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    bio = TextAreaField("Bio")
    picture = FileField(
        "Update Profile Picture", validators=[FileAllowed(["jpg", "png"])]
    )
    submit = SubmitField("Update")

    def validate_username(self, username):
        """Validator to ensure the new username does not already exist in the database"""

        if username.data != current_user.username:
            # Only check if the username is different from the current one
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    "Username already exists! Please choose a different one"
                )

    def validate_email(self, email):
        """Validator to ensure the new email does not already exist in the database"""

        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    "Email already exists! Please choose a different one"
                )


class RequestResetForm(FlaskForm):
    """Form to request a password reset"""

    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            # Password requirements: 1 lowercase, 1 uppercase, 1 number, 1 special character, 8-32 characters
            Regexp(
                r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#_])[A-Za-z\d@$!%*?&#_]{8,32}$"
            ),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Reset Password")
