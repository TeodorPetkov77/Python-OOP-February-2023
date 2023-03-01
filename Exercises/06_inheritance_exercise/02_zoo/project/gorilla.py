from project.bear import Bear
from project.lizard import Lizard
from project.mammal import Mammal


class Gorilla(Mammal):
    def __init__(self, name):
        super().__init__(name)


mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)

# https://judge.softuni.org/Contests/Compete/Index/1941#1

# 2.	Zoo
# Create a zoo project that contains the following classes:
# Submit in judge a zip file of the project, containing a separate file for each of the classes using the structure shown below:
#
# Follow the diagram and create all the classes. Except for the Animal class, each class should inherit from another class, as shown in the diagram. The Animal class should receive a name - string upon initialization.
# Every class should have a constructor, which accepts one parameter: name
# Test Code	Output
# mammal = Mammal("Stella")
# print(mammal.__class__.__bases__[0].__name__)
# print(mammal.name)
# lizard = Lizard("John")
# print(lizard.__class__.__bases__[0].__name__)
# print(lizard.name)	Animal
# Stella
# Reptile
# John