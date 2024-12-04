# library.py

from models import Book, User, Author

class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.authors = {}

    # Book Operations
    def add_book(self, title, author, genre, publication_date):
        if title in self.books:
            raise ValueError("Book already exists.")
        if author not in self.authors:
            raise ValueError("Author does not exist. Please add the author first.")
        book = Book(title, author, genre, publication_date)
        self.books[title] = book

    def borrow_book(self, library_id, title):
        if library_id not in self.users:
            raise ValueError("User does not exist.")
        if title not in self.books:
            raise ValueError("Book does not exist.")
        book = self.books[title]
        if book.borrow_book():
            self.users[library_id].borrow_book(title)
        else:
            raise ValueError("Book is already borrowed.")

    def return_book(self, library_id, title):
        if library_id not in self.users:
            raise ValueError("User does not exist.")
        if title not in self.books:
            raise ValueError("Book does not exist.")
        book = self.books[title]
        book.return_book()
        self.users[library_id].return_book(title)

    def search_book(self, title):
        return self.books.get(title, None)

    def display_all_books(self):
        return list(self.books.values())

    # User Operations
    def add_user(self, name, library_id):
        if library_id in self.users:
            raise ValueError("Library ID already exists.")
        user = User(name, library_id)
        self.users[library_id] = user

    def view_user_details(self, library_id):
        return self.users.get(library_id, None)

    def display_all_users(self):
        return list(self.users.values())

    # Author Operations
    def add_author(self, name, biography):
        if name in self.authors:
            raise ValueError("Author already exists.")
        author = Author(name, biography)
        self.authors[name] = author

    def view_author_details(self, name):
        return self.authors.get(name, None)

    def display_all_authors(self):
        return list(self.authors.values())
