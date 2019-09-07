from main import db


class EmployeeModel(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(), nullable=False, unique=True)
    gender = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    phoneNumber = db.Column(db.String(), nullable=False)
    idNumber = db.Column(db.Integer(), nullable=False, unique=True)
    kraPin = db.Column(db.String(), nullable=False, unique=True)
    basicSalary = db.Column(db.Float(), nullable=False)
    benefits = db.Column(db.Float(), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))

    def create_record(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def id_number_exists(cls, natId):
        record = cls.query.filter_by(idNumber=natId)

        if record.first():
            return True
        else:
            return False

    @classmethod  # method bound to a class rather than object
    def fetch_all_emps(cls):  # fetch all employees
        return cls.query.all()  # similar to EmployeeModel.query.all

    # edit by id
    @classmethod
    def edit_employee_by_id(cls, id, fullName=None, gender=None, email=None, phoneNumber=None, idNumber=None,
                      kraPin=None, basicSalary=None, benefits=None, department_id=None):
        record = cls.query.filter_by(id=id).first()

        if record:
            record.fullName = fullName
            record.gender = gender
            record.email = email
            record.phoneNumber = phoneNumber
            record.idNumber = idNumber
            record.kraPin = kraPin
            record.basicSalary = basicSalary
            record.benefits = benefits
            record.department_id = department_id
            db.session.commit()
            return True
        else:
            return False

    # delete employee record
    @classmethod
    def delete_employee_by_id(cls, id):
        record = cls.query.filter_by(id=id)

        if record.first():
            record.delete()
            db.session.commit()
            return True

        else:
            return False

    @classmethod
    def fetch_emp_by_id(cls, id):
        return cls.query.filter_by(id=id).first
