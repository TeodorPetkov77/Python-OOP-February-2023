from time import time


def exec_time(func):
    def wrapper(*args):
        start = time()
        func(*args)
        end = time()
        return end - start

    return wrapper


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))


@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1


print(loop())

# 8.	Execution Time
# Import the time module. Create a decorator called exec_time. It should calculate how much time a function needs to be executed. See the examples for more clarification.
# Note: You might have different results from the given ones. The solutions to this problem cannot be submitted in the judge system.
# Examples
# Test Code	Output
# @exec_time
# def loop(start, end):
#     total = 0
#     for x in range(start, end):
#         total += x
#     return total
# print(loop(1, 10000000))	0.8342537879943848
# @exec_time
# def concatenate(strings):
#     result = ""
#     for string in strings:
#         result += string
#     return result
# print(concatenate(["a" for i in range(1000000)]))	0.14537858963012695
# @exec_time
# def loop():
#     count = 0
#     for i in range(1, 9999999):
#         count += 1
# print(loop())	0.4199554920196533
