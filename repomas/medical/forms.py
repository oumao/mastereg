from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, BooleanField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class MedicalStatusForm(FlaskForm):

    height = FloatField('Height', validators=[DataRequired()])
    weight = FloatField('Weight', validators=[DataRequired()])
    disabled = BooleanField('Disability')
    diagnosis = StringField('Disease Diagnosis', validators=[DataRequired()])
    underlying = StringField('Underlying Condition', validators=[DataRequired()])
    drug  = StringField('Drug Administered', validators=[DataRequired()])
    outcome  = StringField('Medical Outcome', validators=[DataRequired()])
    need_referral = BooleanField('Referral Status')

    submit = SubmitField('Register Records')

    


class MedicalStatusUpdateForm(FlaskForm):

    height = FloatField('Height', validators=[DataRequired()])
    weight = FloatField('Weight', validators=[DataRequired()])
    disabled = BooleanField('Disability', default=False, validators=[DataRequired()])
    diagnosis = StringField('Disease Diagnosis', validators=[DataRequired()])
    underlying = StringField('Underlying Condition', validators=[DataRequired()])
    drug  = StringField('Drug Administered', validators=[DataRequired()])
    outcome  = StringField('Medical Outcome', validators=[DataRequired()])
    need_referral = BooleanField('Referral Status', default=False, validators=[DataRequired()])

    submit = SubmitField('Update Records')


class MedicalFilterForm(FlaskForm):

    searchinput = StringField('Filter', validators=[DataRequired()])

    submit = SubmitField('Search')

