from flask import render_template
from . import student

@student.route('/student/registration', methods=['POST', 'GET'])
def registration():
    return render_template('student/registration', title='Student Registration')

@student.route('/students/', methods=['POST', 'GET'])
def all_students():
    return render_template('student/students.html', title='Students')


@student.route('/student/<int:id>', methods=['POST', 'GET'])
def one_student(id):
    return render_template('student/student.html', title='Student')

@student.route('/students/<int:id>', methods=['POST', 'GET'])
def update_student(id):
    return render_template('student/update.html', title='Student Update')