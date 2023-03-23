def even_numbers(function):

    def wrapper(numbers):

        return list(filter(lambda x: x % 2 == 0, function(numbers)))

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))

# https://judge.softuni.org/Contests/Practice/Index/1946#2

# 3.	Even Numbers
# Having the following code:
#
# Complete the code, so it works as expected.
# Examples
# Test Code	Output
# @even_numbers
# def get_numbers(numbers):
#     return numbers
# print(get_numbers([1, 2, 3, 4, 5]))	[2, 4]
