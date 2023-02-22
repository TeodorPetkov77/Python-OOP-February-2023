class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


shop = Shop("My Shop", [])
print(shop.get_items_count())


# https://judge.softuni.org/Contests/Compete/Index/1935#0
