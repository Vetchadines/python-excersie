class employee:
    base = 10000
    def __init__(self, name, employee_id, sales):
        self.name = name
        self.employee_id = employee_id
        self.sales = sales

    def base_employee(self):
        return employee.base

    def com_emp(self):
        return (employee.base+self.sales)/100

name = input('Enter name: ')
emp_id = int(input('Enter emp id: '))
sales = int(input('Enter sales: '))

b = employee(name,emp_id,sales)
print(b.base_employee())
print(b.com_emp())
