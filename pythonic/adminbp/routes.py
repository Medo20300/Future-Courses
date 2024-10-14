from flask import Blueprint
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from pythonic import admin, db, bcrypt
from pythonic.models import User, Lesson, Course
from flask_admin import AdminIndexView

# Create a new Blueprint named 'adminbp' for organizing admin-related routes and views in the application.
adminbp = Blueprint("adminbp", __name__)

"""
This module sets up the admin interface for managing users, lessons, and courses 
in the application. It uses Flask-Admin to create views for these models and 
restricts access to authenticated users with admin privileges (specifically 
the user with ID 1).

Classes:
1. UserModelView: Customizes the admin view for the User model. It hashes passwords 
   upon creation or update and restricts access to admin users only.
   
2. MyModelView: A base model view for Lesson and Course that restricts access to 
   authenticated users with admin privileges.
   
3. MyAdminIndexView: Custom index view for the admin interface that restricts access 
   to authenticated admins only.
"""

class UserModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8)"
        )

    def is_accessible(self):
        return current_user.is_authenticated and current_user.id == 1


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.id == 1


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.id == 1

# Adding admin views for the User, Lesson, and Course models

admin.add_view(UserModelView(User, db.session))
admin.add_view(MyModelView(Lesson, db.session))
admin.add_view(MyModelView(Course, db.session))
