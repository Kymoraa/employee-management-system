# # TODO: Slide 68
#
# """
# Create a class called Payroll whose major task is to calculate an individual’s Net Salary by getting the inputs
# basic salary and benefits. Create 5 different class methods which will calculate the payee (i.e. Tax),
# NHIFDeductions, NSSFDeductions, grossSalary and netSalary.
# NB: Use KRA, NHIF and NSSF values provided in the link below
# https://www.aren.co.ke/payroll/taxrates.htm
# check definitions: https://www.coverfox.com/personal-finance/tax/salary-calculator/
#
# PAYE:
# Up to 12,298		10
# 12,299 - 23,885	 	15
# 23,886 - 35,472		20
# 35,473 - 47,059		25
# Above 47,059		30
#
# NHIF:
# Gross Pay (Ksh)	Deduction (Ksh)	 	Gross Pay (Ksh)	Deduction (Ksh)
# Up to   5,999	150	 	40,000 - 44,999	1,000
# 6,000 - 7,999	300	 	45,000 - 49,999	1,100
# 8,000 - 11,999	400	 	50,000 - 59,999	1,200
# 12,000 - 14,999	500	 	60,000 - 69,999	1,300
# 15,000 - 19,999	600	 	70,000 - 79,999	1,400
# 20,000 - 24,999	750	 	80,000 - 89,999	1,500
# 25,000 - 29,999	850	 	90,000 - 99,999	1,600
# 30,000 - 34,999	900	 	100,000 and above	1,700
# 35,000 - 39,999	950
#
# NSSF:
# Under the old NSSF Act, the employee and the employer contributed 5% of gross pay each
#
#
# """
#
#
# class Payroll:
#
#     def __init__(self, basic_sal, benefits):
#
#         self.basic_salary = basic_sal
#         self.benefits = benefits
#
#     def calc_gross_sal(self):
#         gross_salary = self.basic_salary + self.benefits
#         return gross_salary
#
#     def calc_payee(self):
#         if employee.calc_gross_sal() <= 12298:
#             payee = (10 * employee.calc_gross_sal())/100
#             return payee
#
#         elif (employee.calc_gross_sal() >= 12299) and (employee.calc_gross_sal() <= 23885):
#             payee = (15 * employee.calc_gross_sal()) / 100
#             return payee
#
#         elif (employee.calc_gross_sal() >= 23886) and (employee.calc_gross_sal() <= 35472):
#             payee = (20 * employee.calc_gross_sal()) / 100
#             return payee
#
#         elif (employee.calc_gross_sal() >= 35473) and (employee.calc_gross_sal() < 47059):
#             payee = (25 * employee.calc_gross_sal()) / 100
#             return payee
#
#         else:
#             payee = (30 * employee.calc_gross_sal()) / 100
#             return payee
#
#     def calc_nhif(self):
#         if employee.calc_gross_sal() <= 5999:
#             nhif = 150
#             return nhif
#
#         elif (employee.calc_gross_sal() >= 6000) and (employee.calc_gross_sal() <= 7999):
#             nhif = 300
#             return nhif
#
#         elif (employee.calc_gross_sal() >= 8000) and (employee.calc_gross_sal() <= 11999):
#             nhif = 400
#             return nhif
#
#         elif (employee.calc_gross_sal() >= 12000) and (employee.calc_gross_sal() <= 14999):
#             nhif = 500
#             return nhif
#
#         elif (employee.calc_gross_sal() >= 15000) and (employee.calc_gross_sal() <= 19999):
#             nhif = 600
#             return nhif
#
#         elif (employee.calc_gross_sal() >= 20000) and (employee.calc_gross_sal() <= 24999):
#             nhif = 750
#             return nhif
#
#         elif (employee.calc_gross_sal() >= 25000) and (employee.calc_gross_sal() <= 29999):
#             nhif = 850
#             return nhif
#
#         elif (employee.calc_gross_sal() >= 30000) and (employee.calc_gross_sal() <= 34999):
#             nhif = 900
#             return nhif
#
#         elif (employee.calc_gross_sal() >= 35000) and (employee.calc_gross_sal() <= 39999):
#             nhif = 950
#             return nhif
#
#         elif (employee.calc_gross_sal() >= 40000) and (employee.calc_gross_sal() <= 44999):
#             nhif = 1000
#             return nhif
#
#         elif (employee.calc_gross_sal() >= 45000) and (employee.calc_gross_sal() <= 49999):
#             nhif = 1100
#             return nhif
#
#         elif (employee.calc_gross_sal() >= 50000) and (employee.calc_gross_sal() <= 59999):
#             nhif = 1200
#             return nhif
#
#         elif (employee.calc_gross_sal() >= 60000) and (employee.calc_gross_sal() <= 69999):
#             nhif = 1300
#             return nhif
#
#         elif (employee.calc_gross_sal() >= 70000) and (employee.calc_gross_sal() <= 79999):
#             nhif = 1400
#             return nhif
#
#         elif (employee.calc_gross_sal() >= 80000) and (employee.calc_gross_sal() <= 89999):
#             nhif = 1500
#             return nhif
#
#         elif (employee.calc_gross_sal() >= 90000) and (employee.calc_gross_sal() <= 99999):
#             nhif = 1600
#             return nhif
#
#         else:
#             nhif = 1700
#             return nhif
#
#     def calc_nssf(self):
#         nssf = (5 * employee.calc_gross_sal())/100
#         return nssf
#
#     def calc_net_sal(self):
#         net_sal = employee.calc_gross_sal() - (employee.calc_payee() + employee.calc_nhif() +
#                                                employee.calc_nssf())
#         return net_sal
#
#
# employee = Payroll(15000, 0)
# print("Gross salary", employee.calc_gross_sal())
# print("PAYE", employee.calc_payee())
# print("NHIF", employee.calc_nhif())
# print("NSSF", employee.calc_nssf())
# print("Net salary", employee.calc_net_sal())


class Payroll:
    basicSalary = 0
    benefits = 0
    grossSalary = 0  # Income before pensionable deduction
    taxableIncome = 0
    nssfContribution = 0
    nhifContribution = 0
    payee = 0  # PAYE : Tax on taxable income
    personal_relief = 1408

    # constructor
    def __init__(self, basic_salary, benefits):
        self.basicSalary = basic_salary
        self.benefits = benefits
        self.calculate_gross_salary()
        self.calculate_nssf()
        self.calculate_nhif()
        self.calculate_taxable_income()
        self.calculate_payee()

    # calculate the gross-salary (bs + benefits)
    def calculate_gross_salary(self):
        # GROSS_SALARY = BASIC_SALARY + BENEFITS
        grossSalary = self.basicSalary + self.benefits

        self.grossSalary = grossSalary

        return grossSalary

    # calculate NSSF pension contribution
    def calculate_nssf(self):
        if 0 < self.grossSalary <= 6000:
            nssf = 0.06 * self.grossSalary
            self.nssfContribution = nssf
            return nssf

        elif 6000 < self.grossSalary < 18000:
            remainder = self.grossSalary - 6000
            nssf = 6000 * 0.06 + remainder * 0.06
            self.nssfContribution = nssf
            return nssf
        elif self.grossSalary > 18000:
            nssf = 6000 * 0.06 + 12000 * 0.06
            self.nssfContribution = nssf
            return nssf

    # calculate NHIF Contribution
    def calculate_nhif(self):
        if 0 <= self.grossSalary <= 5999:  # 0 - 5999
            nhif = 150
            self.nhifContribution = nhif
            return nhif
        elif 6000 <= self.grossSalary <= 7999:  # 6000 - 7999
            nhif = 300
            self.nhifContribution = nhif
            return nhif
        elif 8000 <= self.grossSalary <= 11999:
            nhif = 400
            self.nhifContribution = nhif
            return
        elif 12000 <= self.grossSalary <= 14999:  # 12000 - 14999
            nhif = 500
            self.nhifContribution = nhif
            return nhif
        elif 15000 <= self.grossSalary < 19999:  # 15000 - 19999
            nhif = 600
            self.nhifContribution = nhif
            return nhif

    # calculate the NET SALARY
    def calculate_taxable_income(self):
        # net_taxable_income = Gross_salary -(NSSF pension contribution)

        nti = self.grossSalary - self.nssfContribution  # nti - net taxable income

        # Set the taxable income( income after pension deductions)
        self.taxableIncome = nti

        return nti

    # calculate PAYEE
    def calculate_payee(self):

        tier1 = 12298
        tier2 = 11587
        tier3 = 11587
        tier4 = 11587

        if self.taxableIncome <= 12298:
            tax = self.taxableIncome * 0.1
            self.payee = tax
            return tax
        elif 12299 <= self.taxableIncome <= 23885:
            remainder = self.taxableIncome - 12298
            tax = tier1 * 0.1 + 0.15 * remainder
            self.payee = tax
            return tax
