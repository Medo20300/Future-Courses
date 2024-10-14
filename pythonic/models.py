"""
This module defines the database models for the application using Flask-SQLAlchemy.
It includes the following models:
- User: Represents a user in the application with authentication capabilities.
- Lesson: Represents a lesson created by a user.
- Course: Represents a course that contains multiple lessons.
- Subscriber: Represents a subscriber's email for newsletters or updates.

Each model is defined as a class that inherits from db.Model, and relationships between models are established where necessary.
"""

from datetime import datetime
from pythonic import db, login_manager
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """Model representing a user in the application."""
    
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    permission = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(125), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.png")
    bio = db.Column(db.Text, nullable=True)
    password = db.Column(db.String(60), nullable=False)
    lessons = db.relationship("Lesson", backref="author", lazy=True)


    def get_reset_token(self):
        """Generate a password reset token."""
        
        s = Serializer(current_app.config["SECRET_KEY"], salt="pw-reset")
        return s.dumps({"user_id": self.id})

    @staticmethod
    def verify_reset_token(token, age=3600):
        """Verify the password reset token."""
        
        s = Serializer(current_app.config["SECRET_KEY"], salt="pw-reset")
        try:
            user_id = s.loads(token, max_age=age)["user_id"]
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.fname}', '{self.lname}', '{self.username}', '{self.email}', '{self.image_file}')"


class Lesson(db.Model):
    """Model representing a lesson created by a user."""
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    thumbnail = db.Column(
        db.String(20), nullable=False, default="default_thumbnail.jpg"
    )
    slug = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)

    def __repr__(self):
        return f"Lesson('{self.title}', '{self.date_posted}')"


class Course(db.Model):
    """Model representing a course that contains multiple lessons."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(150), nullable=False)
    icon = db.Column(db.String(20), nullable=False, default="default_icon.jpg")
    lessons = db.relationship("Lesson", backref="course_name", lazy=True)

    def __repr__(self):
        return f"Course('{self.title}')"


class Subscriber(db.Model):
    """Model representing a subscriber's email for updates."""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)

    def __repr__(self):
        return f"Subscriber('{self.email}')"
