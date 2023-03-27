import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Teo", "Zebra", "Eee")

    def test_init(self):
        self.assertEqual(self.mammal.name, "Teo")
        self.assertEqual(self.mammal.type, "Zebra")
        self.assertEqual(self.mammal.sound, "Eee")

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), "Teo makes Eee")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_get_info(self):
        self.assertEqual(self.mammal.info(), "Teo is of type Zebra")


if __name__ == '__main__':
    unittest.main()

# https://judge.softuni.org/Contests/Compete/Index/1949#0
