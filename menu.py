# menu.py

from library import Library
from validators import (
    validate_library_id,
    validate_date,
    validate_non_empty,
    validate_choice
)

class Menu:
    def __init__(self):
        self.library = Library()

    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!\n")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")

            choice = input("Select an option: ")
            if choice == '1':
                self.book_operations_menu()
            elif choice == '2':
                self.user_operations_menu()
            elif choice == '3':
                self.author_operations_menu()
            elif choice == '4':
                print("Thank you for using the Library Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    # Book Operations Menu
    def book_operations_menu(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")

            choice = input("Select an option: ")
            if choice == '1':
                self.add_new_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.search_book()
            elif choice == '5':
                self.display_all_books()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    # User Operations Menu
    def user_operations_menu(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")

            choice = input("Select an option: ")
            if choice == '1':
                self.add_new_user()
            elif choice == '2':
                self.view_user_details()
            elif choice == '3':
                self.display_all_users()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    # Author Operations Menu
    def author_operations_menu(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")

            choice = input("Select an option: ")
            if choice == '1':
                self.add_new_author()
            elif choice == '2':
                self.view_author_details()
            elif choice == '3':
                self.display_all_authors()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    # Book Operations Methods
    def add_new_book(self):
        try:
            title = input("Enter book title: ").strip()
            if not validate_non_empty(title):
                raise ValueError("Title cannot be empty.")

            author = input("Enter author name: ").strip()
            if not validate_non_empty(author):
                raise ValueError("Author name cannot be empty.")

            genre = input("Enter genre: ").strip()
            if not validate_non_empty(genre):
                raise ValueError("Genre cannot be empty.")

            publication_date = input("Enter publication date (YYYY-MM-DD): ").strip()
            if not validate_date(publication_date):
                raise ValueError("Invalid date format.")

            self.library.add_book(title, author, genre, publication_date)
            print(f"Book '{title}' added successfully.")
        except ValueError as ve:
            print(f"Error: {ve}")

    def borrow_book(self):
        try:
            library_id = input("Enter your Library ID: ").strip()
            if not validate_library_id(library_id):
                raise ValueError("Invalid Library ID format.")

            title = input("Enter the title of the book to borrow: ").strip()
            if not validate_non_empty(title):
                raise ValueError("Book title cannot be empty.")

            self.library.borrow_book(library_id, title)
            print(f"Book '{title}' borrowed successfully by user '{library_id}'.")
        except ValueError as ve:
            print(f"Error: {ve}")

    def return_book(self):
        try:
            library_id = input("Enter your Library ID: ").strip()
            if not validate_library_id(library_id):
                raise ValueError("Invalid Library ID format.")

            title = input("Enter the title of the book to return: ").strip()
            if not validate_non_empty(title):
                raise ValueError("Book title cannot be empty.")

            self.library.return_book(library_id, title)
            print(f"Book '{title}' returned successfully by user '{library_id}'.")
        except ValueError as ve:
            print(f"Error: {ve}")

    def search_book(self):
        title = input("Enter the title of the book to search: ").strip()
        book = self.library.search_book(title)
        if book:
            print("\nBook Details:")
            print(book)
        else:
            print("Book not found.")

    def display_all_books(self):
        books = self.library.display_all_books()
        if books:
            print("\nAll Books:")
            for book in books:
                print(book)
        else:
            print("No books available in the library.")

    # User Operations Methods
    def add_new_user(self):
        try:
            name = input("Enter user name: ").strip()
            if not validate_non_empty(name):
                raise ValueError("Name cannot be empty.")

            library_id = input("Enter Library ID (4-10 alphanumeric characters): ").strip()
            if not validate_library_id(library_id):
                raise ValueError("Invalid Library ID format.")

            self.library.add_user(name, library_id)
            print(f"User '{name}' added successfully with Library ID '{library_id}'.")
        except ValueError as ve:
            print(f"Error: {ve}")

    def view_user_details(self):
        library_id = input("Enter Library ID: ").strip()
        user = self.library.view_user_details(library_id)
        if user:
            print("\nUser Details:")
            print(user)
        else:
            print("User not found.")

    def display_all_users(self):
        users = self.library.display_all_users()
        if users:
            print("\nAll Users:")
            for user in users:
                print(user)
        else:
            print("No users registered in the library.")

    # Author Operations Methods
    def add_new_author(self):
        try:
            name = input("Enter author name: ").strip()
            if not validate_non_empty(name):
                raise ValueError("Name cannot be empty.")

            biography = input("Enter biography: ").strip()
            if not validate_non_empty(biography):
                raise ValueError("Biography cannot be empty.")

            self.library.add_author(name, biography)
            print(f"Author '{name}' added successfully.")
        except ValueError as ve:
            print(f"Error: {ve}")

    def view_author_details(self):
        name = input("Enter author name: ").strip()
        author = self.library.view_author_details(name)
        if author:
            print("\nAuthor Details:")
            print(author)
        else:
            print("Author not found.")

    def display_all_authors(self):
        authors = self.library.display_all_authors()
        if authors:
            print("\nAll Authors:")
            for author in authors:
                print(author)
        else:
            print("No authors available in the library.")
