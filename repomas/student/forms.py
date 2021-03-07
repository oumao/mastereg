from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError, DataRequired

from repomas.models import Student


class StudentRegistrationForm(FlaskForm):

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    admission = StringField('Admission Number', validators=[DataRequired()])
    birthdate = DateField('Date of Birth', validators=[DataRequired()])
    zipcode = IntegerField('Zip Code', validators=[DataRequired()])
    county  = StringField('County', validators=[DataRequired()])
    ward = StringField('Ward', validators=[DataRequired()])

    submit = SubmitField('Save Student')

    def validate_admission(self, admission):
        student = Student.query.filter_by(admission=admission.data).first()
        if student:
            raise ValidationError('That admission number is taken. Please choose a different one.')

    


class StudentUpdateForm(FlaskForm):

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    admission = StringField('Admission Number', validators=[DataRequired()])
    birthdate = DateField('Date of Birth', validators=[DataRequired()])
    zipcode = IntegerField('Zip Code', validators=[DataRequired()])
    county  = StringField('County', validators=[DataRequired()])
    ward = StringField('Ward', validators=[DataRequired()])

    submit = SubmitField('Update Details')
