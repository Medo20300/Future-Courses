from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed  # Importing FlaskForm to create forms, and FileField to handle file uploads
from pythonic.models import Course
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import (
    DataRequired, # DataRequired ensures that a field is not left empty. 
    Length,  # Length limits the character length of input, 
    ValidationError,  # and ValidationError is used to raise custom validation errors.
)


class NewCourseForm(FlaskForm):
    """Defining the form for creating a new course"""

    title = StringField("Course Name", validators=[DataRequired(), Length(max=50)])
    description = TextAreaField(
        "Course Description", validators=[DataRequired(), Length(max=150)]
    )
    icon = FileField("Icon", validators=[DataRequired(), FileAllowed(["jpg", "png"])])
    submit = SubmitField("Create")

    def validate_title(self, title):
        """Custom validation function to check if the course name already exists in the database"""

        # Query the Course model to find a course with the same title.
        course = Course.query.filter_by(title=title.data).first()

        # If a course with the same title exists, raise a ValidationError with a custom message.
        if course:
            raise ValidationError(
                "Course name already exists! Please choose a different one"
            )
