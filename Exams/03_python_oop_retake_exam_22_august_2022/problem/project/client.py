class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: list = []  # will contain objects
        self.bill: float = 0  # total amount of money for all meals that the client has added to his shopping cart

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if value[0] != "0" or len(value) != 10 or not all((x.isnumeric() for x in value)):
            raise ValueError("Invalid phone number!")
        self.__phone_number = value

    def reset_order(self):
        self.shopping_cart = []
        self.bill = 0
