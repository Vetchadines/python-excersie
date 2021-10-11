class AIBBank:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdrawl(self, amount):
        if 0 < amount <=self.balance:
            self.balance -= amount
            return amount
        return 0

    def query_balance(self):
        return '{} You have {} euro in your account'.format(self.customer_name, self.balance)

