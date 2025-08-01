# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # starts as available

    def check_out(self):  # ✅ fix: no space in def
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # already checked out

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out


class Library:   # ✅ you were missing this entire class!
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"'{title}' has been checked out.")
                return
        print(f"'{title}' is not available.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' was not checked out.")

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
