import bankaccount

customer= input('Enter Customer Name: ')
bankaccount1 = bankaccount.AIBBank(customer)

bankaccount1.deposit(5000)

bankaccount1.withdrawl(1000)

print(bankaccount1.query_balance())

print(bankaccount1.balance)
