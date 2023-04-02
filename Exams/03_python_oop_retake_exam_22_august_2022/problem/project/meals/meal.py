from abc import ABC, abstractmethod


class Meal(ABC):
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.default_quantity = self.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be an empty string!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Invalid price!")
        self.__price = value

    @abstractmethod
    def details(self):
        ...

    def reset_quantity(self):
        self.quantity = self.default_quantity

    def set_new_default(self):
        self.default_quantity = self.quantity
