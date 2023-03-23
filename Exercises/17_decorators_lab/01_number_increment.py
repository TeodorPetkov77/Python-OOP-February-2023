def number_increment(numbers):

    def increase():

        return [x + 1 for x in numbers]

    return increase()


print(number_increment([1, 2, 3]))

# https://judge.softuni.org/Contests/Practice/Index/1946#0

# 1.	Number Increment
# Having the following code:
#
# Complete the code, so it works as expected.
# Examples
# Test Code	Output
# print(number_increment([1, 2, 3]))	[2, 3, 4]
