from flask import Blueprint
import secrets
import os
from pythonic.models import Lesson, Course
from flask_ckeditor import upload_success, upload_fail
from flask_login import current_user
from flask import (
    render_template,
    url_for,
    request,
    send_from_directory,
)
from flask import current_app


main = Blueprint("main", __name__)


@main.route("/files/<path:filename>")
def uploaded_files(filename):
    path = os.path.join(current_app.root_path, "static/media")
    return send_from_directory(path, filename)


@main.route("/upload", methods=["POST"])
def upload():
    f = request.files.get("upload")
    extension = f.filename.split(".")[-1].lower()
    if extension not in ["jpg", "gif", "png", "jpeg"]:
        return upload_fail(message="File extension not allowed!")
    random_hex = secrets.token_hex(8)
    image_name = random_hex + extension
    f.save(os.path.join(current_app.root_path, "static/media", image_name))
    url = url_for("main.uploaded_files", filename=image_name)
    return upload_success(url, filename=image_name)


@main.route("/")
@main.route("/home")
def home():

    current_name = None
    # Initialize admin_permission as False by default
    admin_permission = False

    # Check if the user is authenticated first
    if current_user.is_authenticated:

        current_name = current_user.fname # show user first name

        if current_user.id == 1:
            # Render the admin page if the user is admin (id == 1)
            return render_template("admin.html", title='Admin Page')
        elif current_user.id > 1:
            # Set admin_permission to True for non-admin authenticated users
            admin_permission = True

    # Fetch lessons and courses for non-admin users or unauthenticated users
    lessons = Lesson.query.order_by(Lesson.date_posted.desc()).paginate(page=1, per_page=6)
    courses = Course.query.paginate(page=1, per_page=6)

    return render_template("home.html", 
                           lessons=lessons, 
                           courses=courses, 
                           admin_permission=admin_permission,
                           current_name=current_name)


@main.route("/about")
def about():
    return render_template("about.html", title="About")

