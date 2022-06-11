from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import UserRegistrationForm, UserLoginForm
from ..utils import generate_uuid

from repomas import db
from repomas.models import User
from . import user


@user.route('/first/registration', methods=['POST', 'GET'])
def first_time_registration():
    user = User.query.filter_by(id=1).first()

    if user:
        return redirect(url_for('user.login'))
    else:

        form = UserRegistrationForm()

        if form.validate_on_submit():
            hashed_pass = generate_password_hash(form.password.data)
            new_user = User(first_name=form.first_name.data, last_name=form.last_name.data,
                            email=form.email.data, username=form.username.data, password=hashed_pass)

            db.session.add(new_user)
            db.session.commit()

            flash("Administrator Successfully Added", "success")
            return redirect(url_for('user.login'))

        return render_template('user/registration.html', form=form)


@user.route('/registration', methods=['POST', 'GET'])
def registration():
    user = User.query.filter_by(id=1).first()

    if user:
        return redirect(url_for('user.login'))
    elif len(User.query.all()) >= 1:

        form = UserRegistrationForm()

        if form.validate_on_submit() and not User.query.filter_by(username=form.email.data):
            hashed_pass = generate_password_hash(form.password.data)
            new_user = User(first_name=form.first_name.data, last_name=form.last_name.data,
                            email=form.email.data, uuid=generate_uuid(), password=hashed_pass)

            db.session.add(new_user)
            db.session.commit()

            flash("Administrator Successfully Added", "success")
            return redirect(url_for('user.login'))

        return render_template('user/registration.html', form=form)
    else:
        return redirect('user.first_registration')


@user.route('/user/login', methods=['POST', 'GET'])
def login():
    form = UserLoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Login Success", "success")
            return redirect(url_for('user.dashboard'))
        else:
            flash("Wrong credentials!!. Please check your email and password and try again!",
                  "danger")
            return redirect(url_for('user.login'))

    return render_template('user/login.html', form=form)


@user.route('/user/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template("user/dashboard.html", title="User Dashboard")


@user.route('/user/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have successfully Logged Out', 'success')
    return redirect(url_for('user.login'))
