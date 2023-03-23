def type_check(type_to_check):
    def decorator(function):
        def wrapper(parameter):
            if isinstance(parameter, type_to_check):
                return function(parameter)
            else:
                return "Bad Type"

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

# https://judge.softuni.org/Contests/Compete/Index/1947#3

# 4.	Type Check
# Create a decorator called type_check. It should receive a type (int/float/str/…), and it should check if the parameter passed to the decorated function is of the type given to the decorator. If it is, execute the function and return the result, otherwise return "Bad Type".
# Examples
# Test Code	Output
# @type_check(int)
# def times2(num):
#     return num*2
# print(times2(2))
# print(times2('Not A Number'))	4
# Bad Type
# @type_check(str)
# def first_letter(word):
#     return word[0]
#
# print(first_letter('Hello World'))
# print(first_letter(['Not', 'A', 'String']))	H
# Bad Type
