from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        valid_types = {"Desktop Computer": DesktopComputer, "Laptop": Laptop}
        if type_computer not in valid_types:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        new_pc = valid_types[type_computer](manufacturer, model)
        message = new_pc.configure_computer(processor, ram)
        self.warehouse.append(new_pc)
        return message

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_memory: int):
        try:
            found_pc = next(filter(lambda x: x.price <= client_budget
                                             and x.processor == wanted_processor
                                             and x.ram >= wanted_memory, self.warehouse))
        except StopIteration:
            raise Exception("Sorry, we don't have a computer for you.")

        self.profits += client_budget - found_pc.price
        self.warehouse.remove(found_pc)

        return f"{found_pc} sold for {client_budget}$."


# computer_store = ComputerStoreApp()
# print(computer_store.build_computer("Desktop Computer", "Dell", "Shitbook", "AMD Ryzen 7 5700G", 128))
# print(computer_store.sell_computer(10000, "AMD Ryzen 7 5700G", 32))
