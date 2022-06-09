from datetime import datetime
from email.policy import default
from repomas import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(uuid):
    return User.query.get(str(uuid))


class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    uuid = db.Column(db.String(80), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return f"<Admin: {self.first_name} {self.last_name} {self.email} {self.username}>"


class Student(db.Model):

    __tablename__ = "students"
    __searchable__ = ['admission']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    admission = db.Column(db.String(20), nullable=False, unique=True)
    birthdate = db.Column(db.DateTime, nullable=False)
    zipcode = db.Column(db.String(10), nullable=False)
    county = db.Column(db.String(15), nullable=False)
    ward = db.Column(db.String(15), nullable=False)
    medicalstat = db.relationship('MedicalStatus', backref='student', lazy='dynamic')

    def __repr__(self) -> str:
        return f"<Student: {self.first_name}, {self.last_name}>"


class MedicalStatus(db.Model):

    __tablename__ = 'medicalstatus'
    __searchable__ = ['diagnosis', 'outcome', 'need_referral', 'disabled']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    disabled = db.Column(db.Boolean, nullable=False, default=False)
    diagnosis = db.Column(db.String(100), nullable=False)
    underlying = db.Column(db.String(50), nullable=False)
    drug = db.Column(db.String(50), nullable=False)
    outcome = db.Column(db.String(50), nullable=False)
    need_referral = db.Column(db.Boolean, nullable=False, default=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

    def __repr__(self) -> str:
        return f"<Medical Status: {self.height}, {self.weight}, {self.disabled}>"


   
