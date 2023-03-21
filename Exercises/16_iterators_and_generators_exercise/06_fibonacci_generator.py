def fibonacci():
    previous_nums = [0, 1]
    while True:
        yield previous_nums[0]
        previous_nums[0], previous_nums[1] = \
            previous_nums[1], sum(previous_nums)


generator = fibonacci()
for i in range(20):
    print(next(generator))

# https://judge.softuni.org/Contests/Compete/Index/1945#5

# 6.	Fibonacci Generator
# Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely. The first two numbers in the sequence are always 0 and 1. Each following Fibonacci number is created by the sum of the current number with the previous one.
# Note: Submit only the function in the judge system
# Examples
# Test Code	Output
# generator = fibonacci()
# for i in range(5):
#     print(next(generator))	0
# 1
# 1
# 2
# 3
# generator = fibonacci()
# for i in range(1):
#     print(next(generator))	0