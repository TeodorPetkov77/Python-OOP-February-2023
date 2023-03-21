class vowels:
    def __init__(self, string_input: str):
        self.string_input = "".join(filter(lambda x: x.lower() in "aeoyiu", string_input))
        self.length = len(self.string_input)
        self.index = 0
        self.vowels = "aeoyiu"

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.length:
            index = self.index
            self.index += 1
            return self.string_input[index]
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

# https://judge.softuni.org/Contests/Practice/Index/1944#2

# 3.	Vowels
# Create a class called vowels, which should receive a string. Implement the __iter__ and __next__ methods, so the iterator returns only the vowels from the string.
# Note: Submit only the class in the judge system
# Examples
# Test Code	Output
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)	A
# e
# i
# u
# y
# o
