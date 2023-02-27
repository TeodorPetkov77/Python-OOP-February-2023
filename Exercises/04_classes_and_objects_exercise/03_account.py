class Account:
    def __init__(self, id, name, balance=0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


# https://judge.softuni.org/Contests/Compete/Index/1937#2

# 3.	Account
# Create a class called Account. Upon initialization, it should receive an id (number), a name (string), and a balance (integer; optional; 0 by default). The class should also have 3 additional instance methods:
# -	credit(amount) - adds the amount to the balance and returns the new balance
# -	debit(amount) - if the amount is less than or equal to the balance, reduces the balance by the amount and returns the new balance. Otherwise, return "Amount exceeded balance"
# -	info() - returns "User {name} with account {id} has {balance} balance"
# Examples
# Test Code	Output
# account = Account(1234, "George", 1000)
# print(account.credit(500))
# print(account.debit(1500))
# print(account.info())	1500
# 0
# User George with account 1234 has 0 balance
# account = Account(5411256, "Peter")
# print(account.debit(500))
# print(account.credit(1000))
# print(account.debit(500))
# print(account.info())	Amount exceeded balance
# 1000
# 500
# User Peter with account 5411256 has 500 balance