def logged(function):
    def wrapper(*args):
        return f"you called {function.__name__}({', '.join(list(map(str, args)))})\n" \
               f"it returned {function(*args)}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))

# https://judge.softuni.org/Contests/Compete/Index/1947#0

# 1.	Logged
# Create a decorator called logged. It should return the name of the function that is being called and its parameters. It should also return the result of the execution of the function being called. See the examples for more clarification.
# Examples
# Test Code	Output
# @logged
# def func(*args):
#     return 3 + len(args)
# print(func(4, 4, 4))	you called func(4, 4, 4)
# it returned 6
# @logged
# def sum_func(a, b):
#     return a + b
# print(sum_func(1, 4))	you called sum_func(1, 4)
# it returned 5
