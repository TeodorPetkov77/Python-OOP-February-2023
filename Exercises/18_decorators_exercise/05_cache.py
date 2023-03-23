def cache(func):
    log_dict = {}

    def wrapper(n):
        if n not in log_dict:
            log_dict[n] = func(n)
        return func(n)

    wrapper.log = log_dict
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)

# https://judge.softuni.org/Contests/Compete/Index/1947#4

# 5.	Cache
# Create a decorator called cache. It should store all the returned values of the recursive function fibonacci. You are provided with this code:
#
# You need to create a dictionary called log that will store all the n's (keys) and the returned results (values) and attach that dictionary to the fibonacci function as a variable called log, so when you call it, it returns that dictionary. For more clarification, see the examples
# Examples
# Test Code	Output
# fibonacci(3)
# print(fibonacci.log)	{1: 1, 0: 0, 2: 1, 3: 2}
# fibonacci(4)
# print(fibonacci.log)	{1: 1, 0: 0, 2: 1, 3: 2, 4: 3}
