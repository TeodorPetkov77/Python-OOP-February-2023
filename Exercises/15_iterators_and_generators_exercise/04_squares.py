def squares(n):
    for i in range(1, n + 1):
        yield i * i


print(list(squares(5)))

# https://judge.softuni.org/Contests/Practice/Index/1944#3

# 4.	Squares
# Create a generator function called squares that should receive a number n. It should generate the squares of all numbers from 1 to n (inclusive).
# Note: Submit only the function in the judge system
# Examples
# Test Code	Output
# print(list(squares(5)))	[1, 4, 9, 16, 25]
