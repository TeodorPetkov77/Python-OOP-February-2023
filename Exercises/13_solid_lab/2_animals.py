class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


class Cat(Animal):
    @staticmethod
    def make_sound():
        return "Meow"


class Dog(Animal):
    @staticmethod
    def make_sound():
        return "Dog"


class Cow(Animal):
    @staticmethod
    def make_sound():
        return "Mooooooooooooooooooo"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat('cat'), Cow('cow'), Dog('dog')]
animal_sound(animals)


# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.species == 'cat':
#             print('meow')
#         elif animal.species == 'dog':
#             print('woof-woof')
#
#
# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)
#
# ## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
# ## при добавяне на нови животни
# # animals = [Animal('cat'), Animal('dog'), Animal('chicken')]