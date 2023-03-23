from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

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

    @property
    @abstractmethod
    def computer_type(self):
        pass

    @property
    @abstractmethod
    def available_cpus(self):
        pass

    @property
    @abstractmethod
    def max_ram(self):
        pass

    @property
    def available_ram(self):
        available_ram = {}
        max_ram = self.max_ram
        while max_ram >= 2:
            available_ram[max_ram] = 0
            max_ram //= 2
        power = len(available_ram)

        for key in available_ram.keys():
            available_ram[key] = power * 100
            power -= 1

        return available_ram

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.available_cpus:
            raise ValueError(
                f"{processor} is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")

        if ram not in self.available_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with "
                             f"{self.computer_type} {self.manufacturer} {self.model}!")

        self.price += self.available_cpus[processor]
        self.processor = processor
        self.price += self.available_ram[ram]
        self.ram = ram

        return f"Created {self.manufacturer} {self.model} with " \
               f"{self.processor} and {self.ram}GB RAM for {self.price}$."

    def __repr__(self):
        return f"{self.__manufacturer} {self.__model} with " \
               f"{self.processor} and {self.ram}GB RAM"
