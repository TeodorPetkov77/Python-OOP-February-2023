from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.max_ram = 128
        self.available_cpus = {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800
        }
        self.processor: str or None = None
        self.ram: int or None = None
        self.price: int = 0
        self.__available_ram = {}

    def configure_computer(self, processor: str, ram: int):

        if processor not in self.available_cpus:
            raise ValueError(f"{processor} is not compatible with desktop "
                             f"computer {self.manufacturer} {self.model}!")

        if ram not in self.available_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with "
                             f"desktop computer {self.manufacturer} {self.model}!")

        self.price += self.available_cpus[processor]
        self.processor = processor
        self.price += self.available_ram[ram]
        self.ram = ram

        return f"Created {self.manufacturer} {self.model} " \
               f"with {self.processor} and {self.ram}GB RAM for {self.price}$."

    @property
    def available_ram(self):

        while self.max_ram >= 2:
            self.__available_ram[self.max_ram] = 0
            self.max_ram //= 2
        power = len(self.__available_ram)

        for key in self.__available_ram.keys():
            self.__available_ram[key] = power * 100
            power -= 1

        return self.__available_ram
