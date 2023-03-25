def even_parameters(function):
    def wrapper(*args):
        check = any(filter(lambda x: not isinstance(x, int) or x % 2 != 0, args))
        if check:
            return "Please use only even numbers!"
        return function(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 2))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

# https://judge.softuni.org/Contests/Compete/Index/1947#1

# 2.	Even Parameters
# Create a decorator function called even_parameters. It should check if all parameters passed to a function are even numbers and only then execute the function and return the result. Otherwise, don't execute the function and return "Please use only even numbers!"
# Examples
# Test Code	Output
# @even_parameters
# def add(a, b):
#     return a + b
#
# print(add(2, 4))
# print(add("Peter", 1))	6
# Please use only even numbers!
# @even_parameters
# def multiply(*nums):
#     result = 1
#     for num in nums:
#         result *= num
#     return result
#
# print(multiply(2, 4, 6, 8))
# print(multiply(2, 4, 9, 8))	384
# Please use only even numbers!
