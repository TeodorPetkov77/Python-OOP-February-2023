from project.cat import Cat


class Tomcat(Cat):
    __gender = "Male"

    def __init__(self, name, age):
        super().__init__(name, age, gender=self.__gender)

    @staticmethod
    def make_sound():
        return "Hiss"

# https://judge.softuni.org/Contests/Compete/Index/1943#4

# 5.	Animals
# Your task is to create a class hierarchy like the one described below. Submit in judge a zip file named project, containing a separate file for each of the classes.
# The Animal class (abstract) should take, attributes, a name, an age, and a gender. It should have 2 methods: repr() and make_sound().
# The Dog class should inherit and implement the Animal class. Its repr() method should return "This is {name}. {name} is a {age} year old {gender} {class}". The dog sound is "Woof!".
# The Cat class should inherit and implement the Animal class. Its repr() method should return "This is {name}. {name} is a {age} year old {gender} {class}". The cat sound, "Meow meow!".
# The Kitten class should inherit and implement the Cat class. Its gender is "Female", and its sound is "Meow".
# The Tomcat class should inherit and implement the Cat class. Its gender is "Male", and its sound is "Hiss".
# Examples
# Test Code	Output
# dog = Dog("Rocky", 3, "Male")
# print(dog.make_sound())
# print(dog)
# tomcat = Tomcat("Tom", 6)
# print(tomcat.make_sound())
# print(tomcat)	Woof!
# This is Rocky. Rocky is a 3 year old Male Dog
# Hiss
# This is Tom. Tom is a 6 year old Male Tomcat
#
# kitten = Kitten("Kiki", 1)
# print(kitten.make_sound())
# print(kitten)
# cat = Cat("Johnny", 7, "Male")
# print(cat.make_sound())
# print(cat)	Meow
# This is Kiki. Kiki is a 1 year old Female Kitten
# Meow meow!
# This is Johnny. Johnny is a 7 year old Male Cat
