def vowel_filter(function):

    def wrapper():

        vowels = ['a', 'e', 'i', 'o', 'y']

        return [x for x in function() if x in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())

# https://judge.softuni.org/Contests/Practice/Index/1946#1

# 2.	Vowel Filter
# Having the following code:
#
# Complete the code, so it works as expected:
# Examples
# Test Code	Output
# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]
#
# print(get_letters())	["a", "e"]
