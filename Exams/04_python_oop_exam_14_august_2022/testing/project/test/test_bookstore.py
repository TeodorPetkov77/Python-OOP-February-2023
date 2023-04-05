from project.bookstore import Bookstore
import unittest


class TestBookstore(unittest.TestCase):
    def setUp(self):
        self.store = Bookstore(10)

    def test_init(self):
        self.assertEqual(self.store.books_limit, 10)
        self.assertEqual(self.store.availability_in_store_by_book_titles, {})
        self.assertEqual(self.store.total_sold_books, 0)

    def test_books_limit_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.store_invalid_book_limit = Bookstore(0)
        self.assertEqual(str(ve.exception), "Books limit of 0 is not valid")

    def test_len(self):
        self.store.receive_book("Book1", 5)
        self.assertEqual(len(self.store), 5)
        self.store.receive_book("Book2", 5)
        self.assertEqual(len(self.store), 10)

    def test_receive_book(self):
        self.assertEqual(self.store.receive_book("Book1", 5), "5 copies of Book1 are available in the bookstore.")
        self.assertEqual(self.store.receive_book("Book1", 2), "7 copies of Book1 are available in the bookstore.")
        self.assertEqual(self.store.receive_book("Book2", 2), "2 copies of Book2 are available in the bookstore.")
        self.assertEqual(self.store.availability_in_store_by_book_titles, {"Book1": 7, "Book2": 2})
        self.assertEqual(str(self.store), "Total sold books: 0\n"
                                          "Current availability: 9\n"
                                          " - Book1: 7 copies\n"
                                          " - Book2: 2 copies")

    def test_receive_book_limit_reached(self):
        with self.assertRaises(Exception) as ex:
            self.store.receive_book("Book1", 11)
        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")
        self.assertEqual(str(self.store), "Total sold books: 0\n"
                                          "Current availability: 0")

    def test_sell_book(self):
        self.store.receive_book("Book1", 5)
        self.store.receive_book("Book2", 2)
        self.assertEqual(self.store.sell_book("Book1", 5), "Sold 5 copies of Book1")
        self.assertEqual(self.store.sell_book("Book2", 1), "Sold 1 copies of Book2")
        self.assertEqual(self.store.availability_in_store_by_book_titles, {"Book1": 0, "Book2": 1})
        self.assertEqual(self.store.total_sold_books, 6)
        self.assertEqual(len(self.store), 1)
        self.assertEqual(str(self.store), "Total sold books: 6\n"
                                          "Current availability: 1\n"
                                          " - Book1: 0 copies\n"
                                          " - Book2: 1 copies")

    def test_sell_book_not_available(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Book1", 5)
        self.assertEqual(str(ex.exception), "Book Book1 doesn't exist!")
        self.assertEqual(self.store.total_sold_books, 0)
        self.assertEqual(len(self.store), 0)
        self.assertEqual(self.store.availability_in_store_by_book_titles, {})
        self.assertEqual(str(self.store), "Total sold books: 0\n"
                                          "Current availability: 0")

    def test_sell_book_not_enough_copies(self):
        self.store.receive_book("Book1", 5)
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Book1", 6)
        self.assertEqual(str(ex.exception), "Book1 has not enough copies to sell. Left: 5")
        self.assertEqual(self.store.total_sold_books, 0)
        self.assertEqual(len(self.store), 5)
        self.assertEqual(self.store.availability_in_store_by_book_titles, {'Book1': 5})
        self.assertEqual(str(self.store), "Total sold books: 0\n"
                                          "Current availability: 5\n"
                                          " - Book1: 5 copies")


if __name__ == '__main__':
    unittest.main()

# https://judge.softuni.org/Contests/Practice/Index/3558#2

