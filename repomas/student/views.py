from flask import render_template
from . import student

@student.route('/student/registration', methods=['POST', 'GET'])
def registration():
    return render_template('student/registration', title='Student Registration')