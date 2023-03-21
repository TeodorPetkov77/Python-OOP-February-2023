class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current = 0
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current + 1 <= self.count:
            current_number = self.number
            self.current += 1
            self.number += self.step
            return current_number
        else:
            raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)


numbers = take_skip(10, 5)
for number in numbers:
    print(number)

# https://judge.softuni.org/Contests/Compete/Index/1945#0

# 1.	Take Skip
# Create a class called take_skip. Upon initialization, it should receive a step (int) and a count (int). Implement the __iter__ and __next__ functions. The iterator should return the count numbers (starting from 0) with the given step. For more clarification, see the examples:
# Note: Submit only the class in the judge system
# Examples
# Test Code	Output
# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)	0
# 2
# 4
# 6
# 8
# 10
# numbers = take_skip(10, 5)
# for number in numbers:
#     print(number)	0
# 10
# 20
# 30
# 40
