from project.computer_types.desktop_computer import DesktopComputer


class Laptop(DesktopComputer):
    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)
        self.max_ram = 64
        self.available_cpus = {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200
        }

    def configure_computer(self, processor: str, ram: int):

        if processor not in self.available_cpus:
            raise ValueError(f"{processor} is not compatible with laptop "
                             f"{self.manufacturer} {self.model}!")

        if ram not in self.available_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with "
                             f"laptop {self.manufacturer} {self.model}!")

        self.price += self.available_cpus[processor]
        self.processor = processor
        self.price += self.available_ram[ram]
        self.ram = ram

        return f"Created {self.manufacturer} {self.model} " \
               f"with {self.processor} and {self.ram}GB RAM for {self.price}$."
