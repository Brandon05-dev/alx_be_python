# library_system.py

class Book:
    def __init__(self, title: str, author: str):
        """Initialize the base Book class"""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of a Book"""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize EBook, calling the base class constructor"""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of an EBook"""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize PrintBook, calling the base class constructor"""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of a PrintBook"""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize Library with an empty list of books"""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library"""
        self.books.append(book)

    def list_books(self):
        """Print all books in the library"""
        for book in self.books:
            print(book)
