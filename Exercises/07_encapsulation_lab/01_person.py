class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

# https://judge.softuni.org/Contests/Practice/Index/1938#0

# 1.	Person
# Create a class called Person. Upon initialization, it should receive a name and an age. Name mangle the name and the age attributes (should not be accessed outside the class). Create two instance methods called get_name and get_age to return the values of the private attributes.
# Examples
# Test Code	Output
# person = Person("George", 32)
# print(person.get_name())
# print(person.get_age())	George
# 32