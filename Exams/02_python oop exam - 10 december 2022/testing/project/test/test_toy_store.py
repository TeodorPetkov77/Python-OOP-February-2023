from project.toy_store import ToyStore
import unittest


class TestToyStore(unittest.TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_init(self):
        self.assertEqual(self.store.toy_shelf, {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None})

    def test_add_toy_shelf_not_exist(self):
        with self.assertRaises(Exception) as error:
            self.store.add_toy("Z", "Car")
        self.assertEqual(str(error.exception), "Shelf doesn't exist!")

    def test_add_toy_toy_already_on_shelf(self):
        self.store.add_toy("A", "Car")
        with self.assertRaises(Exception) as error:
            self.store.add_toy("A", "Car")
        self.assertEqual(str(error.exception), "Toy is already in shelf!")

    def test_add_toy_shelf_already_taken(self):
        self.store.add_toy("A", "Car")
        with self.assertRaises(Exception) as error:
            self.store.add_toy("A", "Truck")
        self.assertEqual(str(error.exception), "Shelf is already taken!")

    def test_add_toy_valid(self):
        self.assertEqual(self.store.add_toy("A", "Car"), "Toy:Car placed successfully!")
        self.assertEqual(self.store.toy_shelf, {'A': 'Car', 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None})

    def test_remove_shell_does_not_exist(self):
        with self.assertRaises(Exception) as error:
            self.store.remove_toy("Z", "Car")
        self.assertEqual(str(error.exception), "Shelf doesn't exist!")

    def test_remove_toy_not_on_shelf(self):
        with self.assertRaises(Exception) as error:
            self.store.remove_toy("A", "Car")
        self.assertEqual(str(error.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_valid(self):
        self.store.add_toy("A", "Car")
        self.assertEqual(self.store.remove_toy("A", "Car"), "Remove toy:Car successfully!")
        self.assertEqual(self.store.toy_shelf["A"], None)
        self.assertEqual(self.store.toy_shelf, {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None})


# # https://judge.softuni.org/Contests/Practice/Index/3728#2
