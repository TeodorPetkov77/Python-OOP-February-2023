import unittest

from cat import Cat


class TestCat(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Kaspar")

    def test_cat_size(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_is_fed(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_if_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as context:
            self.cat.eat()
        self.assertEqual(str(context.exception), 'Already fed.')

    def test_cat_cannot_sleep_if_not_fed(self):
        with self.assertRaises(Exception) as context:
            self.cat.sleep()
        self.assertEqual(str(context.exception), 'Cannot sleep while hungry')

    def test_cannot_sleep_if_not_sleepy(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()

# https://judge.softuni.org/Contests/Practice/Index/1948#1

# 2.	Test Cat
#
# Create a class CatTests
# In judge you need to submit just the CatTests class, with the unitttest module imported.
# Create the following tests:
# •	Cat's size is increased after eating
# •	Cat is fed after eating
# •	Cat cannot eat if already fed, raises an error
# •	Cat cannot fall asleep if not fed, raises an error
# •	Cat is not sleepy after sleeping

