from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import UserRegistrationForm, UserLoginForm
from ..utils import generate_uuid

from repomas import db
from repomas.models import User
from . import user


@user.route('/registration', methods=['POST', 'GET'])
def registration():
    user_count = User.query.count()
    form = UserRegistrationForm()
    if form.validate_on_submit():
        if user_count == 0:
            print("success")
            hashed_pass = generate_password_hash(form.password.data)
            admin = User(first_name=form.first_name.data, last_name=form.last_name.data,
                         email=form.email.data, password=hashed_pass,
                         uuid=generate_uuid(), is_admin=True, is_active=True
                         )

            db.session.add(admin)
            db.session.commit()

            flash("Administrator Successfully Added", "success")
            return redirect(url_for('user.login'))
        else:
            hashed_pass = generate_password_hash(form.password.data)
            new_user = User(first_name=form.first_name.data, last_name=form.last_name.data,
                            email=form.email.data, password=hashed_pass, uuid=generate_uuid())
            print(new_user)
            db.session.add(new_user)
            db.session.commit()

            flash("User Successfully Added", "success")
            return redirect(url_for('user.login'))

    return render_template('user/registration.html', form=form, user_count=user_count)


@user.route('/login', methods=['POST', 'GET'])
def login():
    users = User.query.all()

    if len(users) == 0:
        return redirect(url_for('user.registration'))
    form = UserLoginForm()
    if form.validate_on_submit():

        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user and existing_user.is_admin and \
                check_password_hash(existing_user.password, form.password.data):

            login_user(existing_user)
            flash("Login Success", "success")
            return redirect(url_for('admin.dashboard'))
        elif existing_user and not existing_user.is_admin and \
                check_password_hash(existing_user.password, form.password.data):
            login_user(existing_user)
            flash("Login Success", "success")
            return redirect(url_for('user.dashboard'))
        else:
            flash("Wrong credentials!!. Please check your email and password and try again!",
                  "danger")
            return redirect(url_for('user.login'))

    return render_template('user/login.html', form=form)


@user.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template("user/dashboard.html", title="User Dashboard")


@user.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have successfully Logged Out', 'success')
    return redirect(url_for('user.login'))
