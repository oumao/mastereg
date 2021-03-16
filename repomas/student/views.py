from datetime import datetime as dt
from flask import flash, url_for, abort, request
from flask_login import login_required
from repomas.student.forms import StudentRegistrationForm, StudentUpdateForm
from flask import render_template, redirect
from repomas import db
from repomas.models import MedicalStatus, Student
from . import student

@student.route('/student/registration', methods=['POST', 'GET'])
@login_required
def add_student():
    form = StudentRegistrationForm()
    if form.validate_on_submit():

        student = Student(first_name=form.first_name.data, last_name=form.last_name.data, 
                    admission=form.admission.data, birthdate=form.birthdate.data, zipcode=form.zipcode.data,
                    county=form.county.data, ward=form.ward.data)
        db.session.add(student)
        db.session.commit()
        flash("Successfully Added a student", "success")
        return redirect(url_for('admin.dashboard'))

    return render_template('student/register.html', form=form, title='Student Registration')

@student.route('/student/all', methods=['POST', 'GET'])
def all_students():
    students = Student.query.all()
    nums = Student.query.count()
    return render_template('student/students_table.html', title='Students', students=students, nums=nums)


@student.route('/student/<int:student_id>', methods=['POST', 'GET'])
@login_required
def student_detail(student_id):
    student = Student.query.get_or_404(student_id)
    medrec = db.session.query(MedicalStatus.height, MedicalStatus.weight, MedicalStatus.disabled,
                                MedicalStatus.diagnosis, MedicalStatus.underlying, MedicalStatus.drug,
                                MedicalStatus.outcome).join(Student, Student.id == MedicalStatus.student_id).filter_by(id=student_id).first()
    currentyr = dt.utcnow()
    return render_template('student/student_details.html', 
    title='Student', student=student, year=currentyr, medrec=medrec)

@student.route('/students/<int:student_id>/update/', methods=['POST', 'GET'])
@login_required
def update_student(student_id):

    student = Student.query.get_or_404(student_id)

    if not student:
        abort(403)

    form = StudentUpdateForm()

    if form.validate_on_submit():

        student.first_name = form.first_name.data
        student.last_name = form.last_name.data
        student.admission = form.admission.data
        student.birthdate = form.birthdate.data
        student.zipcode = form.zipcode.data
        student.county = form.county.data
        student.ward = form.ward.data

        db.session.commit()

        flash("Successfully Updated the student", "success")
        return redirect(url_for('student.all_students'))

    elif request.method == 'GET':

        form.first_name.data = student.first_name
        form.last_name.data = student.last_name
        form.admission.data = student.admission
        form.birthdate.data = student.birthdate
        form.zipcode.data = student.zipcode
        form.county.data = student.county
        form.ward.data = student.ward

    return render_template('student/register.html', title='Student Update', 
                                    legend="Update Student Details", form=form)

@student.route('/student/<int:student_id>/delete/', methods=['POST', 'GET'])
@login_required
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    if student:
        db.session.delete(student)
        db.session.commit()
        flash("Successfully deleted the student from the database", "success")
        return redirect(url_for('student.all_students'))
    else:
        flash("The student does not exist", "warning")
        return redirect(url_for('student.all_students')) 