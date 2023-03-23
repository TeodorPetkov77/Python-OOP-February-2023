from typing import List
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse: List = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        valid_types = {"Desktop Computer": DesktopComputer, "Laptop": Laptop}
        if type_computer not in valid_types:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        self.warehouse.append(valid_types[type_computer](manufacturer, model))
        return self.warehouse[-1].configure_computer(processor, ram)

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        found_pc = [x for x in self.warehouse if x.price <= client_budget
                    and x.processor == wanted_processor
                    and x.ram >= wanted_ram]
        if not found_pc:
            raise Exception("Sorry, we don't have a computer for you.")
        self.profits += client_budget - found_pc[0].price
        self.warehouse.remove(found_pc[0])
        return f"{found_pc[0]} sold for {client_budget}$."

#
# computer_store = ComputerStoreApp()
# print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
# print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))


# 93/100 TO BE REWORKED