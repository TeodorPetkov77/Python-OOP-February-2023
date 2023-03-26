class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.iterable[self.index]
        else:
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

# https://judge.softuni.org/Contests/Practice/Index/1944#1

# 2.	Reverse Iter
# Create a class called reverse_iter which should receive an iterable upon initialization. Implement the __iter__ and __next__ methods, so the iterator returns the items of the iterable in reversed order.
# Note: Submit only the class in the judge system
# Examples
# Test Code	Output
# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)	4
# 3
# 2
# 1
