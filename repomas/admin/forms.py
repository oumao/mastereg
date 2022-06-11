from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError

from repomas.models import User

class UpdateForm(FlaskForm):
    pass
