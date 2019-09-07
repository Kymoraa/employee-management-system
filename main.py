from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from resources.emp_payroll import Payroll


# import the configs
from config.configs import DevelopmentConfig, ProductionConfig, Config

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# instantiate SQLAlchemy
db = SQLAlchemy(app)

# import the models
from models.department import DepartmentModel
from models.employee import EmployeeModel


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/employees', methods=['GET','POST'])
def employees():
    if request.method == 'POST':
        name = request.form['full_name']
        gender = request.form['gender']
        email = request.form['email']
        phone = request.form['phone']
        dpt_id = request.form['department']
        id_number = request.form['id_number']
        kra_pin = request.form['kra_pin']
        basic_salary = request.form['basic_salary']
        benefits = request.form['benefits']

        if EmployeeModel.id_number_exists(id_number):
            # print("Already Exists")
            flash('The record already exists','danger')
            return redirect(url_for('employees'))

        else:
            emp = EmployeeModel(fullName=name, gender=gender, email=email, phoneNumber=phone,
                                department_id=dpt_id, idNumber=id_number, kraPin=kra_pin,
                                basicSalary=basic_salary, benefits=benefits)
            emp.create_record()
            # print("Success")
            flash('Employee successfully added', 'success')
            return redirect(url_for('employees'))

    all_emps = EmployeeModel.fetch_all_emps()
    all_depts = DepartmentModel.fetch_all_depts()

    return render_template('employees.html', emps=all_emps, dpts=all_depts)


@app.route('/departments', methods=['GET', 'POST'])
def departments():

    all_depts = DepartmentModel.fetch_all_depts()

    if request.method == 'POST':
        name = request.form['department']
        print(name)

        if DepartmentModel.check_dept_exists(name):
            flash('Department already exists', 'danger')

        else:
            record = DepartmentModel(name=name)
            record.create()
            flash('Department successfully added', 'success')
            return redirect(url_for('departments'))

    return render_template('departments.html', dpts=all_depts)


# page to display all employees in a particular department
@app.route('/departments/employees/<int:id>', methods=['GET', 'POST'])
def department_employees(id):
    dept_emps = DepartmentModel.fetch_by_id(id)
    emp = dept_emps.employee  # fetch employees in a particular department fetched by id

    return render_template('dept_emps.html', wafanyikazi=emp, dep=dept_emps)


@app.route('/employee/edit/<int:id>', methods=['POST'])
def edit_employees(id):
    if request.method == 'POST':
        name = request.form['full_name']
        gender = request.form['gender']
        email = request.form['email']
        phone = request.form['phone']
        dpt_id = request.form['department']
        id_number = request.form['id_number']
        kra_pin = request.form['kra_pin']
        basic_salary = request.form['basic_salary']
        benefits = request.form['benefits']

        update = EmployeeModel.edit_employee_by_id(id=id, fullName=name, gender=gender, email=email, phoneNumber=phone,
                                                   idNumber=id_number, kraPin=kra_pin, basicSalary=basic_salary,
                                                   benefits=benefits,department_id=dpt_id)

        if update:
            print('update successful')
            return redirect(url_for('employees'))
        else:
            print('record not found')
            return redirect(url_for('employees'))


@app.route('/employee/delete/<int:id>', methods=['POST'])
def delete_employees(id):
    delete = EmployeeModel.delete_employee_by_id(id)

    if delete:
        print('deleted successfully')
        return redirect(url_for('employees'))

    else:
        print('unable to delete record at this time')
        return redirect(url_for('employees'))


@app.route('/department/edit/<int:id>', methods=['POST'])
def edit_department(id):
    if request.method == 'POST':
        name = request.form['department']

        update = DepartmentModel.edit_department_by_id(id=id, name=name)
        if update:
            flash('Update successful', 'success')
            return redirect(url_for('departments'))
        else:
            flash('Unable to edit the department', 'danger')
            return redirect(url_for('departments'))


@app.route('/generate_payroll/<int:id>', methods=['POST'])
def generate_payroll(id):
    an_employee = EmployeeModel.fetch_emp_by_id(id)

    if request.method == 'POST':
        month = request.form['month']
        basic = float(request.form['basic'])
        benefit = float(request.form['benefit'])

    pay = Payroll(basic_salary=basic, benefits=benefit)
    gross = pay.calculate_gross_salary()
    print('GROSS SALARY:', gross)

    nssf = pay.calculate_nssf()
    print('NSSF CONTRIBUTION:', nssf)

    # the income after pension deduction = grossSalary - nssfContribution
    taxable_income = pay.calculate_taxable_income()
    print('Income after pension deduction(taxable income', taxable_income)

    # tax on the taxable income
    paye = pay.calculate_payee()
    print('PAYE(Tax on taxable income):', paye)

    personal_relief = pay.personal_relief
    print('Personal relief:', personal_relief)

    # some missing code here...... to be continued

    return 'Payroll generated'


if __name__ == '__main__':
    app.run(debug=True)
