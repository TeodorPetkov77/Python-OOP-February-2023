from abc import ABC, abstractmethod


class IFormatter(ABC):
    @abstractmethod
    def format(self, book):
        pass


class IPrinter(ABC):
    @abstractmethod
    def get_book(self, book):
        pass


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter(IFormatter):
    def format(self, book) -> str:
        return book.content


class Printer(IPrinter):
    def get_book(self, book):
        formatter = Formatter()
        formatted_book = formatter.format(book)
        return formatted_book


# class Book:
#     def __init__(self, content: str):
#         self.content = content
#
#
# class Formatter:
#     def format(self, book: Book) -> str:
#         return book.content
#
#
# class Printer:
#     def get_book(self, book: Book):
#         formatter = Formatter()
#         formatted_book = formatter.format(book)
#         return formatted_book