from project.animals.animal import Mammal
from project.food import Vegetable, Meat, Fruit


class Mouse(Mammal):
    def allowed_foods(self):
        return [Fruit, Vegetable]

    def weight_per_food(self):
        return 0.1

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    def allowed_foods(self):
        return [Meat]

    def weight_per_food(self):
        return 0.4

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    def allowed_foods(self):
        return [Meat, Vegetable]

    def weight_per_food(self):
        return 0.3

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    def allowed_foods(self):
        return [Meat]

    def weight_per_food(self):
        return 1

    @staticmethod
    def make_sound():
        return "ROAR!!!"
