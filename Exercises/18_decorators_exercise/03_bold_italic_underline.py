def make_bold(function):
    def wrapper(*args):
        return f"<b>{function(*args)}</b>"

    return wrapper


def make_italic(function):
    def wrapper(*args):
        return f"<i>{function(*args)}</i>"

    return wrapper


def make_underline(function):
    def wrapper(*args):
        return f"<u>{function(*args)}</u>"

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))

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
