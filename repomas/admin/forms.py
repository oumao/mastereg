from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, FloatField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email, Length



class AdminRegistrationForm(FlaskForm):
    
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),
                            EqualTo('password')])

    submit = SubmitField('Register')



class AdminLoginForm(FlaskForm):
    
    username = StringField('First Name', validators=[DataRequired()])
    password = PasswordField('First Name', validators=[DataRequired(), Length(min=6, max=20)])

    submit = SubmitField('Login')