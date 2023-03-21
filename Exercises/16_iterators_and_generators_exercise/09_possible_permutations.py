from itertools import permutations


def possible_permutations(sequence):
    for pos_list in list(permutations(sequence)):
        yield list(pos_list)


[print(n) for n in possible_permutations([1, 2, 3, 4, 5])]

# https://judge.softuni.org/Contests/Compete/Index/1945#8

# 9.	Possible permutations
# Create a generator function called possible_permutations() which should receive a list and return lists with all possible permutations between its elements.
# Note: Submit only the function in the judge system
# Examples
# Test Code	Output
# [print(n) for n in possible_permutations([1, 2, 3])]	[1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]
# [print(n) for n in possible_permutations([1])]	[1]
