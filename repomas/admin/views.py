from flask import render_template
from . import admin

@admin.route('/admin/registration', methods=['POST', 'GET'])
def registration():
    return render_template('home.html')