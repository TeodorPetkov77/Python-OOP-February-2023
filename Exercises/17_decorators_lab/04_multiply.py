def multiply(times):

    def decorator(function):

        def wrapper(number):
            
            return times * function(number)

        return wrapper

    return decorator


def add_ten(number):
    return number + 10


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))

# https://judge.softuni.org/Contests/Practice/Index/1946#3

# 4.	Multiply
# Having the following code:
#
# Complete the code, so it works as expected.
# Examples
# Test Code	Output	Comment
# @multiply(3)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(3))	39	First, we add 3 to 10 = 13, and then we multiply the result by 3: 13 * 3 = 39
# @multiply(5)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(6))	80	(6 + 10) * 5 = 80
