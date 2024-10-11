<!DOCTYPE html>
<html>>
<body>
    <h1>Future Courses</h1>
</body>


</html>

# Introduction

## is a fully integrated web application built using the Flask framework, with a MySQL database for backend support. This project offers a range of functionalities, including course management, lesson handling, user authentication (registration and login), and error management. It also integrates tools like CKEditor for rich text editing.

# Key Features

 *  User System:
 *  User registration and login functionality.
 *  User account management.
 *  Course and Lesson Management:
 *  Display available courses.
 *  Add new lessons to courses.
 *  Edit existing lessons.
 *  CKEditor Integration:
 *  Provides a rich text editor for creating and formatting content.
 *  Error Handling:
 *  A comprehensive error handling system to manage application-level exceptions.

# Project Structure

### Here is a brief overview of the key directories and files in the project:

* adminbp/: Contains routes and logic for admin-related actions.
* courses/: Handles routes and forms related to course and lesson management.
* errors/: Contains the logic for error handling.
* main/: Includes the primary routes and functions for the main interface.
* static/: Stores static files like images, icons, and the CKEditor plugin.
* models.py: Defines the database models for user and course management.
* config.py: Contains the configuration settings for the Flask application, such as database connections.

# Installation

1. Clone the repository:

* git clone https://github.com/Medo20300/Future-Courses.git

2. Create and activate a virtual environment:

* python3 -m venv venv
* source venv/bin/activate

3. Install the required dependencies:

* pip install -r requirements.txt

4. Configure the database:

* Ensure you have MySQL installed.
* Create the database using the script provided in config.py and update the credentials as needed.

5. Run the application:

* flask run

# Technologies Used

* Backend: Flask (Python)
* Database: MySQL
* Frontend: HTML, CSS, JavaScript
* Text Editor: CKEditor
* Version Control: Git, GitHub

# Future Enhancements

1. Implementing a more advanced user role management system (e.g., admins, instructors, students).
2. Adding API endpoints to allow interaction with mobile apps or external services.
3. Enhancing course content with multimedia support.

# Author
1. Medhat Mohamed Deif - [medhatconcrete@gmail.com](mailto:medhatconcrete@gmail.com)
2. Bishoy Hany Halim - [bishoyhany31@gmail.com](mailto:bishoyhany31@gmail.com)

