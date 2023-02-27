class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user):

        for book in self.books_available[author]:
            if book == book_name:
                user.books.append(book)
                self.books_available[author].remove(book)
                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}
                self.rented_books[user.username][book_name] = days_to_return
                return f"{book_name} successfully rented for the " \
                       f"next {days_to_return} days!"

        for username, books in self.rented_books.items():
            for book, days in books.items():
                if book == book_name:
                    return f'The book "{book_name}" is already rented ' \
                           f'and will be available in {days} days!'

    def return_book(self, author: str, book_name: str, user):

        if book_name in user.books:
            user.books.remove(book_name)
            self.rented_books[user.username].pop(book_name)
            self.books_available[author].append(book_name)

        else:
            return f"{user.username} doesn't have this book in his/her records!"


