from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import AdminRegistrationForm, AdminLoginForm

from repomas import db
from ..models import Admin
from . import admin
    

@admin.route('/', methods=['POST', 'GET'])
def registration():

    admin = Admin.query.filter_by(id=1).first()

    if admin:
        return redirect(url_for('home.login'))
    else:

        form = AdminRegistrationForm()

        if form.validate_on_submit():

            hashed_pass = generate_password_hash(form.password.data)
            new_admin = Admin(first_name=form.first_name.data, last_name=form.last_name.data,
                        email=form.email.data, username=form.username.data, password=hashed_pass)

            db.session.add(new_admin)
            db.session.commit()
            
            flash("Administrator Successfully Added", "success")
            return redirect(url_for('home.login'))
            
        return render_template('admin/registration.html', form=form)

    

@admin.route('/admin/login', methods=['POST', 'GET'])
def login():
    
    form = AdminLoginForm()
    if form.validate_on_submit():

        admin = Admin.query.filter_by(username=form.username.data).first()

        if admin and check_password_hash(admin.password, form.password.data):
            login_user(admin)
            flash("Login Succes", "success")
            return redirect(url_for('home.dashboard'))
        else:
            flash("There is no administrator with such credentials!!. Please check your details and try again", "danger")
            return redirect(url_for('home.login'))

    return render_template('admin/login.html', form=form)
   



@admin.route('/admin/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("admin/dashboard.html", title="Admin Dashboard")