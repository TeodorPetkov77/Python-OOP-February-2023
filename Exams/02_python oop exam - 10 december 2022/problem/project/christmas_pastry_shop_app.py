from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: list = []
        self.delicacies: list = []
        self.income: float = 0

    @property
    def valid_delicacies(self):
        return {
            "Gingerbread": Gingerbread,
            "Stolen": Stolen
        }

    @property
    def valid_booths(self):
        return {
            "Open Booth": OpenBooth,
            "Private Booth": PrivateBooth
        }

    def add_delicacy(self, type_delicacy: str, name: str, price: float):

        name_exist = [n for n in self.delicacies if n.name == name]

        if name_exist:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.valid_delicacies.keys():
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = self.valid_delicacies[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        number_exist = [b for b in self.booths if b.booth_number == booth_number]

        if number_exist:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.valid_booths.keys():
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = self.valid_booths[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        found_booth = [b for b in self.booths
                       if b.capacity >= number_of_people
                       and b.is_reserved is False]

        if not found_booth:
            raise Exception(f"No available booth for {number_of_people} people!")

        found_booth = found_booth[0]
        found_booth.reserve(number_of_people)
        return f"Booth {found_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):

        found_booth = [b for b in self.booths if b.booth_number == booth_number]
        found_delicacy = [d for d in self.delicacies if d.name == delicacy_name]

        if not found_booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not found_delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        found_booth = found_booth[0]
        found_delicacy = found_delicacy[0]

        found_booth.order_delicacy(found_delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        found_booth = [b for b in self.booths if b.booth_number == booth_number][0]
        bill = found_booth.get_total_cost()
        self.income += bill
        found_booth.free()
        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

# https://judge.softuni.org/Contests/Practice/Index/3728#1
