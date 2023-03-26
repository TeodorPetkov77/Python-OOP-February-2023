import unittest

from extended_list import IntegerList


class TestIntegerList(unittest.TestCase):
    def setUp(self):
        self.test_list = IntegerList(1, 2, 3, 3.5, "9")

    def test_init(self):
        self.assertEqual(self.test_list.get_data(), [1, 2, 3])

    def test_add_integer(self):
        self.assertEqual(self.test_list.add(4), [1, 2, 3, 4])

    def test_add_non_integer(self):
        with self.assertRaises(ValueError) as context:
            self.test_list.add(4.5)
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_remove_valid_index(self):
        self.assertEqual(self.test_list.remove_index(0), 1)

    def test_remove_index_out_of_range(self):
        with self.assertRaises(IndexError) as context:
            self.test_list.remove_index(3)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_get_valid_index(self):
        self.assertEqual(self.test_list.get(0), 1)

    def test_get_index_out_of_range(self):
        with self.assertRaises(IndexError) as context:
            self.test_list.get(3)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_valid_index(self):
        self.test_list.insert(0, 0)
        self.assertEqual(self.test_list.get_data(), [0, 1, 2, 3])

    def test_insert_index_out_of_range(self):
        with self.assertRaises(IndexError) as context:
            self.test_list.insert(3, 4)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_non_integer(self):
        with self.assertRaises(ValueError) as context:
            self.test_list.insert(2, "4")
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_get_biggest(self):
        self.assertEqual(self.test_list.get_biggest(), 3)

    def test_index(self):
        self.assertEqual(self.test_list.get_index(3), 2)


if __name__ == '__main__':
    unittest.main()

# https://judge.softuni.org/Contests/Practice/Index/1948#2

# 3.	List
# You are provided with a class IntegerList. It should only store integers. The initial integers should be set by the constructor. They are stored as a list. IntegerList has a functionality to add, remove_index, get, insert, get the biggest number, and get the index of an element. Your task is to test the class.
# Note: You are not allowed to change the structure of the provided code
# Constraints
# •	add operation, should add an element and returns the list.
# o	If the element is not an integer, a ValueError is thrown
# •	remove_index operation removes the element on that index and returns it.
# o	If the index is out of range, an IndexError is thrown
# •	__init__ should only take integers, and store them
# •	get should return the specific element
# o	If the index is out of range, an IndexError is thrown
# •	insert
# o	If the index is out of range, IndexError is thrown
# o	If the element is not an integer, ValueError is thrown
# •	get_biggest
# •	get_index
# Hint
# Do not forget to test the constructor
