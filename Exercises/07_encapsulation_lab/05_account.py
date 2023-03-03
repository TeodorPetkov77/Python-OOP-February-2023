class Account:
    def __init__(self, id, balance, pin):
        self.__id = id
        self.__pin = pin
        self.balance = balance

    def get_id(self, pin):
        if pin == self.__pin:
            return self.__id
        else:
            return "Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        else:
            return "Wrong pin"

# https://judge.softuni.org/Contests/Practice/Index/1938#4

# 5.	Account
# Create a class called Account. Upon initialization, it should receive an id, a balance, and a pin (all numbers). The pin and the id should be private instance attributes, and the balance should be a public attribute. Create two public instance methods:
# •	get_id(pin) - if the given pin is correct, return the id, otherwise, return "Wrong pin"
# •	change_pin(old_pin, new_pin) - if the old pin is correct, change it to the new one and return "Pin changed", otherwise return "Wrong pin"
# Examples
# Test Code	Output
# account = Account(8827312, 100, 3421)
# print(account.get_id(1111))
# print(account.get_id(3421))
# print(account.balance)
# print(account.change_pin(2212, 4321))
# print(account.change_pin(3421, 1234))	Wrong pin
# 8827312
# 100
# Wrong pin
# Pin changed