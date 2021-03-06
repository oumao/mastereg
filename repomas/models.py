from repomas import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(int(user_id))

class Admin(db.Model, UserMixin):

    __tablename__ = "administrator"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.string(15), nullable=False)
    last_name = db.Column(db.string(15), nullable=False)
    email = db.Column(db.string(20), nullable=False, unique=True)
    username = db.Column(db.string(15), nullable=False, unique=True)
    password = db.Column(db.string(80), nullable=False)

    def __repr__(self) -> str:
        return "<Admin: {0} {1} {2} {3}>".format(self.first_name, self.last_name, 
        self.email, self.username)



class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.string(15), nullable=False)
    last_name = db.Column(db.string(15), nullable=False)
    admission = db.Column(db.string(15), nullable=False, unique=True)
    birthdate = db.Column(db.DateTime, nullable=False)
    address = db.relationship('Address', backref='student', lazy='dynamic')


class Address(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    zipcode = db.Column(db.string(10), nullable=False)
    county = db.Column(db.string(15), nullable=False)
    home_address = db.Column(db.string(15), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)

   
