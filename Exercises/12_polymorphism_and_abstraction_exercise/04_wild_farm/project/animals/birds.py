from project.animals.animal import Bird
from project.food import Meat, Vegetable, Seed, Fruit


class Owl(Bird):
    def allowed_foods(self):
        return [Meat]

    def weight_per_food(self):
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    def allowed_foods(self):
        return [Meat, Vegetable, Seed, Fruit]

    def weight_per_food(self):
        return 0.35

    @staticmethod
    def make_sound():
        return "Cluck"
