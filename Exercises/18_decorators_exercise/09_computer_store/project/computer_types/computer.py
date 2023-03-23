from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor: str or None = None
        self.ram: int or None = None
        self.price: int = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        self.processor = processor
        self.ram = ram

    def __repr__(self):
        return f"{self.__manufacturer} {self.__model} with " \
               f"{self.processor} and {self.ram}GB RAM"



