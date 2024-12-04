# models.py

import datetime

class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True

    # Getters and Setters
    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def get_publication_date(self):
        return self.__publication_date

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def is_available(self):
        return self.__is_available

    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False

    def return_book(self):
        self.__is_available = True

    def __str__(self):
        status = "Available" if self.__is_available else "Borrowed"
        return (f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, "
                f"Publication Date: {self.__publication_date}, Status: {status}")


class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    # Getters and Setters
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_library_id(self):
        return self.__library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)

    def __str__(self):
        borrowed = ', '.join(self.__borrowed_books) if self.__borrowed_books else "None"
        return f"Name: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {borrowed}"


class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    # Getters and Setters
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_biography(self):
        return self.__biography

    def set_biography(self, biography):
        self.__biography = biography

    def __str__(self):
        return f"Name: {self.__name}, Biography: {self.__biography}"
