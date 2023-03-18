from project.cat import Cat


class Kitten(Cat):
    __gender = "Female"

    def __init__(self, name, age):
        super().__init__(name, age, gender=self.__gender)

    @staticmethod
    def make_sound():
        return "Meow"
