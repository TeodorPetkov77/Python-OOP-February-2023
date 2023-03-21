class countdown_iterator:
    def __init__(self, count):
        self.count = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count - 1 >= 0:
            self.count -= 1
            return self.count
        else:
            raise StopIteration


# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")


# https://judge.softuni.org/Contests/Compete/Index/1945#2

# 3.	Countdown Iterator
# Create a class called countdown_iterator. Upon initialization, it should receive a count. Implement the iterator to return each countdown number (from count to 0 inclusive), separated by a single space.
# Note: Submit only the class in the judge system
# Examples
# Test Code	Output
# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")	10 9 8 7 6 5 4 3 2 1 0
#
# iterator = countdown_iterator(0)
# for item in iterator:
#     print(item, end=" ")	0
