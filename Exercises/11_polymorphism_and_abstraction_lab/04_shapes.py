from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape, ABC):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return pi * self.__radius ** 2

    def calculate_perimeter(self):
        return pi * self.__radius * 2


class Rectangle(Shape, ABC):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return (self.__height + self.__width) * 2

# https://judge.softuni.org/Contests/Practice/Index/1942#2

# 4.	Shapes
# Create an abstract class Shape with abstract methods calculate_area and calculate_perimeter. Create classes Circle (receives radius upon initialization) and Rectangle (receives height and width upon initialization) that implement those methods (returning the result). The fields of Circle and Rectangle should be private.
# Submit all the classes and your imports in the judge system
# Examples
# Test Code	Output
# circle = Circle(5)
# print(circle.calculate_area())
# print(circle.calculate_perimeter())	78.53981633974483
# 31.41592653589793
# rectangle = Rectangle(10, 20)
# print(rectangle.calculate_area())
# print(rectangle.calculate_perimeter())	200
# 60
