from main import db


class EmployeeModel(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(), nullable=False, unique=True)
    gender = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    phoneNumber = db.Column(db.String(), nullable=False)
    department = db.Column(db.String(), nullable=False)
    idNumber = db.Column(db.Float(), nullable=False, unique=True)
    kraPin = db.Column(db.Float(), nullable=False, unique=True)
    basicSalary = db.Column(db.Float(), nullable=False)
    benefits = db.Column(db.Float(), nullable=False)
