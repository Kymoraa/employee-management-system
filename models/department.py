from main import db


class DepartmentModel(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=True, unique=True)
    employee = db.relationship('EmployeeModel', backref='dept', lazy=True)

    def create(self):
        db.session.add(self)
        db.session.commit()

    # check if the record exists
    @classmethod
    def check_dept_exists(cls, dept_name):
        record = DepartmentModel.query.filter_by(name=dept_name).first()

        if record:
            return True
        else:
            return False

    # fetch all departments
    @classmethod  # method bound to a class rather than object
    def fetch_all_depts(cls):
        return cls.query.all()

    # fetch departments by id
    @classmethod
    def fetch_by_id(cls, dept_id):
        return cls.query.filter_by(id=dept_id).first()

    # edit department by id
    @classmethod
    def edit_department_by_id(cls, id, name=None):
        record = cls.query.filter_by(id=id).first()
        if record:
            record.name = name
            db.session.commit()
            return True
        else:
            return False



