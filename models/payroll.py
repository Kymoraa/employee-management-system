from main import db


class PayrollModel(db.Model):
    __tablename__ = 'payrolls'
    id = db.Column(db.Integer, primary=True)
    gross_salary = db.Column(db.Float)
    net_salary = db.Column(db.Float)
    PAYE = db.Column(db.Float)
    NHIF = db.Column(db.Float)
    NSSF = db.Column(db.Float)
    employee_id = db.Column(db.Integer, db.Foreignkey('employees.id'))

    # create the payroll in the db
    def insert_payroll(self):
        db.session.add(self)
        db.session.commit()

