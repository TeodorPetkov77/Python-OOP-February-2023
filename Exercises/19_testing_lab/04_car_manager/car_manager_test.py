import unittest
from car_manager import Car


class TestCatManager(unittest.TestCase):
    def setUp(self):
        self.car = Car("VW", "Golf", 6, 55)

    def test_init(self):
        self.assertEqual(self.car.make, "VW")
        self.assertEqual(self.car.model, "Golf")
        self.assertEqual(self.car.fuel_consumption, 6)
        self.assertEqual(self.car.fuel_capacity, 55)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_not_valid(self):
        with self.assertRaises(Exception) as error:
            self.car.make = ""
        self.assertEqual(str(error.exception), "Make cannot be null or empty!")

    def test_model_not_valid(self):
        with self.assertRaises(Exception) as error:
            self.car.model = ""
        self.assertEqual(str(error.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_not_valid(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_consumption = 0
        self.assertEqual(str(error.exception), "Fuel consumption cannot be zero or negative!")

    def test_capacity_not_valid(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_capacity = 0
        self.assertEqual(str(error.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_not_valid(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_amount = -1
        self.assertEqual(str(error.exception), "Fuel amount cannot be negative!")

    def test_refuel_valid(self):
        self.car.refuel(50)
        self.assertEqual(self.car.fuel_amount, 50)

    def test_refuel_not_valid(self):
        with self.assertRaises(Exception) as error:
            self.car.refuel(0)
        self.assertEqual(str(error.exception), "Fuel amount cannot be zero or negative!")

    def test_drive_valid(self):
        self.car.refuel(7)
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 1)

    def test_drive_not_valid(self):
        with self.assertRaises(Exception) as error:
            self.car.drive(100)
        self.assertEqual(str(error.exception), "You don't have enough fuel to drive!")


if __name__ == '__main__':
    unittest.main()

# https://judge.softuni.org/Contests/Practice/Index/1948#3

# 4.	Car Manager
# You are provided with a simple project containing only one class - Car. The provided class is simple - its main point is to represent some of the functionality of a Car. Each car contains information about its make, model, fuel consumption, fuel amount, and fuel capacity. Also, each Car can add some fuel to its tank by refueling and can travel distance by driving. In order to be driven, our Car needs to have enough fuel. Everything in the provided skeleton is working perfectly fine, and you mustn't change it.
# Your job now is to write unit tests on the provided project and its functionality. You should test every part of the code inside the Car class:
# •	You should test the constructor
# •	You should test all the methods and validations inside the class
# Constraints
# •	Everything in the provided skeleton is working perfectly fine
# •	You must not change anything in the project structure
# •	Any part of validation should be tested
# •	There is no limit on the tests you can write but keep your attention on the main functionality
# Note: You are not allowed to change the structure of the provided code
#
# "Brum…Brum…Brum-suuuututututu…"
