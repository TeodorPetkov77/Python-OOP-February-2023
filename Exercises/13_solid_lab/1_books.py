from typing import List


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self, name):
        self.name = name
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)
        return f"Book {book.title} added."

    def find_book(self, title):
        try:
            book = next(filter(lambda b: b.title == title, self.books))
            return f"Found book \"{book.title}\" by {book.author}!"
        except StopIteration:
            return f"The book \"{title}\" is not in the library."



# class Book:
#     def __init__(self, title, author, location):
#         self.title = title
#         self.author = author
#         self.location = location
#         self.page = 0
#
#     def turn_page(self, page):
#         self.page = page