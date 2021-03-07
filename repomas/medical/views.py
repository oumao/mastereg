from flask import render_template

from repomas.models import Student, MedicalStatus
from .forms import MedicalStatusForm
from . import med

@med.route('/medical/<int:student_id>/add', methods=['POST', 'GET'])
def add_record(student_id):
    student = Student.query.get_or_404(student_id)
    form = MedicalStatusForm()

    return render_template('medical/student_record.html', title='Medical Status', 
                        form=form, student=student)

@med.route('/medical/records', methods=['POST', 'GET'])
def all_records():
    return render_template('student/students.html', title='Medical Status')


@med.route('/medical/<int:id>', methods=['POST', 'GET'])
def student_record(id):
    return render_template('student/student.html', title='Medical Status')

@med.route('/medical/update/<int:id>', methods=['POST', 'GET'])
def update_record(id):
    return render_template('student/update.html', title='Medical Status')

@med.route('/medical/delete/<int:id>', methods=['POST', 'GET'])
def delete_record(id):
    return render_template('student/update.html', title='Medical status')