import os
from flask import current_app


def get_previous_next_lesson(lesson):
    """
    Retrieves the previous and next lessons in the same course relative to the given lesson.
    
    Args:
        lesson: The current lesson object.
    
    Returns:
        tuple: A tuple containing the previous lesson and next lesson objects (or None if they don't exist).
    """
    course = lesson.course_name  # Get the course of the current lesson
    
    # Loop through all lessons in the course to find the current lesson's index
    for lsn in course.lessons:
        if lsn.title == lesson.title:
            index = course.lessons.index(lsn)   # Get the current lesson's index
            previous_lesson = course.lessons[index - 1] if index > 0 else None
            next_lesson = (
                course.lessons[index + 1] if index < len(course.lessons) - 1 else None
            )
            break
    return previous_lesson, next_lesson


def delete_picture(picture_name, path):
    """Deletes a picture file from the specified path"""

    picture_path = os.path.join(current_app.root_path, path, picture_name)
    try:
        os.remove(picture_path)  # Try to delete the picture
    except:
        pass
