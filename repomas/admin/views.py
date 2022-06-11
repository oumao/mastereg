from flask import render_template
from flask_login import login_required, current_user
from repomas import db
from repomas.models import User
from . import admin


@admin.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template("admin/dashboard.html", title="Admin Dashboard")

