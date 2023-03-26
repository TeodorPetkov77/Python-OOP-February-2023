class custom_range:
    def __init__(self, start: int, end: int):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            current = self.current
            self.current += 1
            return current
        else:
            raise StopIteration


one_to_ten = custom_range(0, 10)
for num in one_to_ten:
    print(num)

# https://judge.softuni.org/Contests/Practice/Index/1944#0

# 1.	Custom Range
# Create a class called custom_range that receives a start (int) and an end (int) upon initialization. Implement the __iter__ and __next__ methods, so the iterator returns the numbers from the start to the end (inclusive).
# Note: Submit only the class in the judge system
# Examples
# Test Code	Output
# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)	1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

