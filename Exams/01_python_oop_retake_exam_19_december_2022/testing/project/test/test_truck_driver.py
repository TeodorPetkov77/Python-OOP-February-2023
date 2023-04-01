from project.truck_driver import TruckDriver
import unittest


class TestTruckDriver(unittest.TestCase):
    def setUp(self):
        self.driver = TruckDriver("Teo", 1)

    def test_init(self):
        self.assertEqual(self.driver.name, "Teo")
        self.assertEqual(self.driver.money_per_mile, 1)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_earned_money_props(self):
        with self.assertRaises(ValueError) as error:
            self.driver.earned_money = -1
        self.assertEqual(str(error.exception), "Teo went bankrupt.")
        self.driver.earned_money = 5
        self.assertEqual(self.driver.earned_money, 5)

    def test_add_cargo_offer_valid(self):
        self.assertEqual(self.driver.add_cargo_offer("Sofia", 10), "Cargo for 10 to Sofia was added as an offer.")
        self.assertEqual(self.driver.available_cargos, {"Sofia": 10})
        self.assertEqual(self.driver.add_cargo_offer("Plovdiv", 20), "Cargo for 20 to Plovdiv was added as an offer.")
        self.assertEqual(self.driver.available_cargos, {"Sofia": 10, "Plovdiv": 20})

    def test_add_cargo_offer_already_exists(self):
        self.driver.add_cargo_offer("Sofia", 10)
        with self.assertRaises(Exception) as error:
            self.driver.add_cargo_offer("Sofia", 10)
        self.assertEqual(str(error.exception), "Cargo offer is already added.")

    def test_drive_best_cargo_offer_valid(self):
        self.driver.earned_money = 100000
        self.driver.add_cargo_offer("Sofia", 10)
        self.driver.add_cargo_offer("Plovdiv", 20000)
        self.assertEqual(self.driver.drive_best_cargo_offer(), "Teo is driving 20000 to Plovdiv.")
        self.assertEqual(self.driver.earned_money, 96000)
        self.assertEqual(self.driver.miles, 20000)

    def test_drive_best_cargo_offer_invalid_no_offers_exist(self):
        self.assertEqual(self.driver.drive_best_cargo_offer(), "There are no offers available.")

    def test_repr(self):
        self.assertEqual(str(self.driver), "Teo has 0 miles behind his back.")


if __name__ == '__main__':
    unittest.main()

# https://judge.softuni.org/Contests/Practice/Index/3622#2
