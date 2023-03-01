from project.product import Product
from project.food import Food
from project.drink import Drink


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        try:
            found = [obj for obj in self.products if obj.name == product_name][0]
            return found
        except IndexError:
            pass

    def remove(self, product_name: str):
        try:
            self.products.remove([obj for obj in self.products if obj.name == product_name][0])
        except IndexError:
            pass

    def __repr__(self):
        return "\n".join([f"{prod.name}: {prod.quantity}" for prod in self.products])
