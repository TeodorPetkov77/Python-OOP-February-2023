class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number:
            self.number -= 1
            if self.index == len(self.sequence) - 1:
                self.index = -1
            self.index += 1
            return self.sequence[self.index]
        else:
            raise StopIteration


# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end ='')


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

# https://judge.softuni.org/Contests/Compete/Index/1945#3

# 4.	Sequence Repeat
# Create a class called sequence_repeat which should receive a sequence and a number upon initialization. Implement an iterator to return the given elements, so they form a string with a length - the given number. If the number is greater than the number of elements, then the sequence repeats as necessary. For more clarification, see the examples:
# Examples
# Test Code	Output
# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end ='')	abcab
# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end ='')	I L
