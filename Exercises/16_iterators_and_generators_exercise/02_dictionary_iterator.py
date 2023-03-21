class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.index = 0
        self.end = len(dictionary)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.end:
            index = self.index
            self.index += 1
            return tuple(self.dictionary.keys())[index], tuple(self.dictionary.values())[index]
        else:
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

# https://judge.softuni.org/Contests/Compete/Index/1945#1

# 2.	Dictionary Iterator
# Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object. Implement the iterator to return each key-value pair of the dictionary as a tuple of two elements (the key and the value).
# Note: Submit only the class in the judge system
# Examples
# Test Code	Output
# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)	(1, '1')
# (2, '2')
# result = dictionary_iter({"name": "Peter", "age": 24})
# for x in result:
#     print(x)	("name", "Peter")
# ("age", 24)
