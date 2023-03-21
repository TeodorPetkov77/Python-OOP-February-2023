# def reverse_text(string):
#     for letter in reversed(string):
#         yield letter


def reverse_text(string):
    for index in range(len(string)-1, -1, -1):
        yield string[index]


for char in reverse_text("step"):
    print(char, end='')

# https://judge.softuni.org/Contests/Practice/Index/1944#4

# 6.	Reverse String
# Create a generator function called reverse_text that receives a string and yields all string characters on one line in reversed order.
# Note: Submit only the function in the judge system
# Examples
# Test Code	Output
# for char in reverse_text("step"):
#     print(char, end='')	pets