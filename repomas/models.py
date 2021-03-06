from repomas import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(int(admin_id))


class Admin(db.Model, UserMixin):

    __tablename__ = "administrator"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self) -> str:
        return "<Admin: {0} {1} {2} {3}>".format(self.first_name, self.last_name, 
        self.email, self.username)



class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    admission = db.Column(db.String(15), nullable=False, unique=True)
    birthdate = db.Column(db.DateTime, nullable=False)
    zipcode = db.Column(db.String(10), nullable=False)
    county = db.Column(db.String(15), nullable=False)
    ward = db.Column(db.String(15), nullable=False)
    medicalstat = db.relationship('MedicalStatus', backref='student', lazy='dynamic')

    def __repr__(self) -> str:
        return "<Student: {0} {1} {2} {3}>".format(
            self.first_name, self.last_name, self.admission, self.birthdate,
            self.zipcode, self.county, self.ward
        )


class MedicalStatus(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    disabled = db.Column(db.Boolean, nullable=False, default=False)
    diagnosis = db.Column(db.String(50), nullable=False)
    underlying = db.Column(db.String(50), nullable=False)
    drug = db.Column(db.String(50), nullable=False)
    outcome = db.Column(db.String(50), nullable=False)
    need_referral = db.Column(db.Boolean, nullable=False, default=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

    def __repr__(self) -> str:
        return "<Medical Status: {} {} {} {} {} {} {} {}>".format(
            self.height, self.weight, self.disabled,
            self.diagnosis, self.underlying, self.drug, 
            self.outcome, self.need_referral
        )


   
