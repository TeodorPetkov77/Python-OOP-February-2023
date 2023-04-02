from typing import List
from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    @property
    def valid_meals(self):
        return ["Dessert", "MainDish", "Starter"]

    def register_client(self, client_phone_number: str):

        phone_exists = [c for c in self.clients_list if
                        c.phone_number == client_phone_number]

        if phone_exists:
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):

        for meal in meals:

            if meal.__class__.__name__ in self.valid_meals:
                self.menu.append(meal)

    def show_menu(self):

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return "\n".join([m.details() for m in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):

        self.show_menu()

        client_exist = [c for c in self.clients_list if
                        c.phone_number == client_phone_number]

        if not client_exist:
            self.register_client(client_phone_number)
            client_exist = self.clients_list[-1]

        else:
            client_exist = client_exist[0]

        for meal_name in meal_names_and_quantities.keys():
            meal_exist = [m for m in self.menu if m.name == meal_name]

            if not meal_exist:
                raise Exception(f"{meal_name} is not on the menu!")

        for meal_name, quantity in meal_names_and_quantities.items():
            quantity_met = [m for m in self.menu if m.quantity >= quantity and m.name == meal_name]

            if not quantity_met:
                meal_type = [m for m in self.menu if m.name == meal_name][0]
                raise Exception(f"Not enough quantity of {meal_type.__class__.__name__}: {meal_name}!")

        for meal_name, quantity in meal_names_and_quantities.items():
            meal_to_add = [m for m in self.menu if m.name == meal_name][0]
            client_exist.shopping_cart.append(meal_to_add)
            client_exist.bill += quantity * meal_to_add.price
            meal_to_add.quantity -= quantity

        meal_names = ", ".join([m.name for m in client_exist.shopping_cart])

        return f"Client {client_phone_number} successfully ordered {meal_names} for {client_exist.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        client.reset_order()

        for meal in self.menu:
            meal.reset_quantity()

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):

        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        FoodOrdersApp.receipt_id += 1

        message = f"Receipt #{FoodOrdersApp.receipt_id} with total amount of {client.bill:.2f} was successfully paid " \
                  f"for {client_phone_number}."

        client.reset_order()

        for meal in self.menu:
            meal.set_new_default()

        return message

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

# https://judge.softuni.org/Contests/Practice/Index/3591#1
