from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def find_area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def find_area(self):
        return self.width * self.height


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def find_area(self):
        return self.side * 2


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def find_area(self):
        return self.radius * pi ** 2


class AreaCalculator:

    def __init__(self, shapes: list):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if isinstance(value, list):
            self.__shapes = value
        else:
            raise ValueError("'shapes should be of type list.'")

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.find_area()

        return total


shapes = [Rectangle(2, 3), Circle(3), Square(4)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

# _____________________________ BEFORE CODE _____________________________

# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
# class AreaCalculator:
#
#     def __init__(self, shapes):
#
#         assert isinstance(shapes, list), "`shapes` should be of type `list`."
#         self.shapes = shapes
#
#     @property
#     def total_area(self):
#         total = 0
#         for shape in self.shapes:
#             total += shape.width * shape.height
#
#         return total
#
#
# shapes = [Rectangle(2, 3), Rectangle(1, 6)]
# calculator = AreaCalculator(shapes)
# print("The total area is: ", calculator.total_area)
