from flask import Blueprint
from pythonic.models import User, Lesson
from flask import (
    render_template,
    url_for,
    flash,
    redirect, # To redirect to different route
    request, # To access request data
)
from pythonic.users.forms import (
    RegistrationForm,
    LoginForm,
    UpdateProfileForm, #  Form to update profile information
    RequestResetForm, # Form to request a password reset
    ResetPasswordForm, # Form to reset the password

)
from pythonic import bcrypt, db  # For password hashing and database access
from flask_login import (
    login_required, # For protecting routes that require login
    login_user,
    current_user, # To access the currently logged-in user
    logout_user,
)
from pythonic.helpers import save_picture  # Helper function to save profile pictures
from pythonic.users.helpers import send_reset_email  # Helper function to send password reset emails

users = Blueprint("users", __name__)


"""Route for user registration"""
@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated: # Redirect if already logged in
        return redirect(url_for("main.home"))
    form = RegistrationForm() # Create an instance of the registration form
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        # Create a new user
        user = User(
            fname=form.fname.data,
            lname=form.lname.data,
            username=form.username.data,
            permission=form.permission.data,
            email=form.email.data,
            password=hashed_password,
        )
        db.session.add(user) # Add the user to the database
        db.session.commit()
        flash(f"Account created successfully for {form.username.data}", "success")
        return redirect(url_for("users.login"))
    return render_template("register.html", title="Register", form=form)


"""Route for user login"""
@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()  # Create an instance of the login form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  # Find the user by email
        if user and bcrypt.check_password_hash(user.password, form.password.data): # Check the password
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            flash("You have been logged in!", "success")
            return redirect(next_page) if next_page else redirect(url_for("main.home"))
        else:
            flash("Login Unsuccessful. Please check credentials", "danger")
    return render_template("login.html", title="Login", form=form)


"""Route to log out the user"""
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))


"""Route to access the dashboard (requires login)"""
@users.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    # Get the user permission from the current logged-in user
    user_permission = current_user.permission  # 'student' or 'mentor'
    admin_permission = current_user.is_authenticated and current_user.id == 1

    if user_permission == 'student':
        return redirect(url_for("users.profile"))

    # Render the appropriate template and pass the user_permission
    return render_template('dashboard.html',
                            title="Dashboard",
                            user_permission=user_permission,
                            admin_permission=admin_permission,
                            active_tab=None)


"""Route for user profile"""
@users.route("/dashboard/profile", methods=["GET", "POST"])
@login_required
def profile():
    profile_form = UpdateProfileForm() # Create an instance of the profile update form
    if profile_form.validate_on_submit():
        if profile_form.picture.data:
            picture_file = save_picture(
                profile_form.picture.data, "static/user_pics", output_size=(150, 150)  
            )
            current_user.image_file = picture_file
 
        current_user.username = profile_form.username.data
        current_user.email = profile_form.email.data
        current_user.bio = profile_form.bio.data
        db.session.commit()  # save the changes to the database
        flash("Your profile has been updated", "success")
        return redirect(url_for("users.profile"))

    elif request.method == "GET":

        profile_form.username.data = current_user.username
        profile_form.email.data = current_user.email
        profile_form.bio.data = current_user.bio

    # Get the path to the user's image
    image_file = url_for("static", filename=f"user_pics/{current_user.image_file}")
    user_permission = current_user.permission  # 'student' or 'mentor'
    admin_permission = current_user.is_authenticated and current_user.id == 1


    return render_template(
        "profile.html",
        title="Profile",
        profile_form=profile_form,
        image_file=image_file,
        active_tab="profile",
        user_permission=user_permission,
        admin_permission=admin_permission,
    )


"""Route to view lessons by a specific author (username)"""
@users.route("/author/<string:username>", methods=["GET"])
def author(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get("page", 1, type=int)
    lessons = (
        Lesson.query.filter_by(author=user)
        .order_by(Lesson.date_posted.desc())
        .paginate(page=page, per_page=6)
    )
    return render_template("author.html", lessons=lessons, user=user)


"""Route to request a password reset"""
@users.route("/reset_password", methods=["GET", "POST"])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RequestResetForm()  # Create an instance of the password reset request form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_reset_email(user)
        flash(
            "If this account exists, you will receive an email with instructions",
            "info",
        )
        return redirect(url_for("users.login"))
    return render_template("reset_request.html", title="Reset Password", form=form)


"""Route to reset the password using a token"""
@users.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    user = User.verify_reset_token(token)
    if not user:
        flash("The token is invalid or expired", "warning")
        return redirect(url_for("users.reset_request"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user.password = hashed_password  # Update the user's password
        db.session.commit()
        flash(f"Your password has been updated. You can now log in", "success")
        return redirect(url_for("users.login"))
    return render_template("reset_password.html", title="Reset Password", form=form)

