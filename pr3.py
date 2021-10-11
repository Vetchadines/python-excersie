class CommissionEmployee:

    def __init__(self, percentage):
        self.percentage = percentage
        self.salary = 0
        self.total_sales = 0

    def calculate_salary(self, sales):
        self.total_sales = sales
        self.salary = self.total_sales * self.percentage
        return self.salary

class BaseSalaryPlusCommission(CommissionEmployee):

    def __init__(self, percentage, base_salary):
        super().__init__(percentage)
        self.base_salary = base_salary

    def calculate_salary(self, sales):
        commission = super().calculate_salary(sales)
        self.salary = commission + self.base_salary
        return self.salary

