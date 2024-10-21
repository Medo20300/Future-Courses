# Importing Blueprint to organize routes, and request to access query parameters in the URL.
from flask import Blueprint, request

from pythonic.models import Lesson, Course
from flask import (
    render_template,
)

# Creating a Blueprint named 'courses' to group the related routes. 
# This helps in structuring the application and making it modular.
courses_bp = Blueprint("courses", __name__)


@courses_bp.route("/<string:course_title>")
def course(course_title):
    # Query the Course model to find a course by its title.
    course = Course.query.filter_by(title=course_title).first()

     # If a course is found, store its ID; otherwise, set course_id to None.
    course_id = course.id if course else None
    course = Course.query.get_or_404(course_id)

    # Get the page number from the URL query parameters. Defaults to page 1 if not specified.
    page = request.args.get("page", 1, type=int)
    lessons = Lesson.query.filter_by(course_id=course_id).paginate(
        page=page, per_page=6
    )
    return render_template(
        "course.html",
        title=course.title,
        course=course,
        lessons=lessons,
    )


@courses_bp.route("/courses")
def courses():
    """courses main route"""

     # Get the page number from the URL query parameters. Defaults to page 1 if not specified.
    page = request.args.get("page", 1, type=int)

    # Query the Course model to paginate and display 6 courses per page.
    courses = Course.query.paginate(page=page, per_page=6)
    return render_template("courses.html", title="Courses", courses=courses)
