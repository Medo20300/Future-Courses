
#    Future Courses

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
-----------------------------------------------------------------------------------------------------------
# Installation

1. Clone the repository:

```python
git clone https://github.com/Medo20300/Future-Courses.git
```

2. Create and activate a virtual environment:

```python
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```python
pip install -r requirements.txt
```

4. Configure the database:

* Ensure you have MySQL installed.
* Create the database using the script provided in config.py and update the credentials as needed.

5. Run the application:

```python
python3 create_app.py
```

```python
python3 run.py
```

------------------------------------------------------------------------------------------------------
# Technologies Used

* Backend: Flask (Python)
* Database: MySQL
* Frontend: HTML, CSS, JavaScript
* Text Editor: CKEditor
* Version Control: Git, GitHub
![FlaskFramework](https://github.com/user-attachments/assets/749d7224-2e3b-4078-9b60-9421bebebae1)
-------------------------------------------------------------------------------------------------------

# Future Enhancements

1. Implementing a more advanced user role management system (e.g., admins, instructors, students).
2. Adding API endpoints to allow interaction with mobile apps or external services.
3. Enhancing course content with multimedia support.


--------------------------------------------------------------------------------------------------------

# Authors

1. **Medhat Mohamed Deif**
   - Role: Full Stack
   - Email: [medhatconcrete@gmail.com](mailto:medhatconcrete@gmail.com)


2. **Bishoy Hany Halim**
   - Role: Full Stack
   - LinkedIn Account: [LinkedIn](https://www.linkedin.com/in/bishoy-hany-halim/)

