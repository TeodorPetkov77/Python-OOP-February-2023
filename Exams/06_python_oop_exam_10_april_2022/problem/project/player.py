from project.supply.supply import Supply


class Player:
    CREATED_USERNAMES = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def need_sustenance(self):
        return self.stamina < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name not valid!")

        if value in Player.CREATED_USERNAMES:
            raise Exception(f"Name {value} is already used!")

        Player.CREATED_USERNAMES.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    def sustain_player(self, food: Supply):
        if self.stamina + food.energy > 100:
            self.stamina = 100
        else:
            self.stamina += food.energy

    def is_stamina_zero(self):
        return self.stamina == 0

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"


