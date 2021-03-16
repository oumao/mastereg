from datetime import datetime as dt
from flask import render_template,flash, redirect, url_for

from repomas import db
from repomas.models import Student, MedicalStatus
from .forms import MedicalStatusForm
from . import med

@med.route('/medical/<int:student_id>/add', methods=['POST', 'GET'])
def add_record(student_id):
    student = Student.query.get_or_404(student_id)
    form = MedicalStatusForm()

    if form.validate_on_submit():
        medrec = MedicalStatus(height=form.height.data, weight=form.weight.data, disabled=form.disabled.data,
                                diagnosis=form.diagnosis.data, underlying=form.underlying.data, drug=form.drug.data,
                                outcome=form.outcome.data, need_referral=form.need_referral.data, student_id=student.id)

        db.session.add(medrec)
        db.session.commit()
        flash("Successfully Added {}'s medical records".format(student.first_name), "success")
        return redirect(url_for('student.student_detail', student_id=student.id))
    return render_template('medical/student_record.html', title='Medical Status', 
                        form=form, student=student)

@med.route('/medical/records', methods=['POST', 'GET'])
def all_records():
    allrec = db.session.query(Student.first_name, Student.last_name, Student.admission, Student.birthdate,
                                MedicalStatus.height, MedicalStatus.weight, MedicalStatus.diagnosis, MedicalStatus.drug,
                                MedicalStatus.underlying, MedicalStatus.need_referral).outerjoin(Student, Student.id==MedicalStatus.student_id).all()
    year = dt.utcnow()
    return render_template('medical/all_records.html', title='Medical Status', allrec=allrec, year=year)


@med.route('/medical/<int:id>', methods=['POST', 'GET'])
def student_record(id):
    return render_template('student/student.html', title='Medical Status')

@med.route('/medical/update/<int:id>', methods=['POST', 'GET'])
def update_record(id):
    return render_template('student/update.html', title='Medical Status')

@med.route('/medical/delete/<int:id>', methods=['POST', 'GET'])
def delete_record(id):
    return render_template('student/update.html', title='Medical status')