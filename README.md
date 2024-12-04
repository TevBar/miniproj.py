Library Management System
The Library Management System is a command-line application built in Python to streamline the management of users and their interactions with library resources. It uses Object-Oriented Programming (OOP) principles to organize its functionality and provides an interface to manage library users, books, and borrowing operations efficiently.

Features
Add new users to the library system with unique IDs.
Borrow and return books using a user's library_id.
View details of all users and their borrowed books.
Ensure robust input validation and error handling.
Requirements
Python 3.7 or higher
Basic understanding of command-line interfaces (CLI)
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
Install any required dependencies:

Note: The current implementation only uses Python's standard library, so no additional dependencies are required.

Run the program:

bash
Copy code
python library_system.py
Usage
Adding a User
Use the add_user method to add a new user to the library system. Each user is assigned a unique library_id.

python
Copy code
library = Library()
library.add_user("Alice")  # Adds a new user named Alice with a unique ID
Borrowing a Book
Users can borrow books by providing their library_id and the book's title.

python
Copy code
library.borrow_book("1001", "1984")  # Alice (ID: 1001) borrows the book "1984"
Returning a Book
To return a borrowed book, use the return_book method (not shown in the provided example but should be implemented similarly to borrowing).

python
Copy code
library.return_book("1001", "1984")  # Alice (ID: 1001) returns the book "1984"
Viewing Users
The self.users dictionary stores user data, including borrowed books.

Example Data Structure
Below is an example of how user data is stored in the system:

python
Copy code
self.users = {
    "1001": {"name": "Alice", "borrowed_books": ["1984", "To Kill a Mockingbird"]},
    "1002": {"name": "Bob", "borrowed_books": []},
}
Error Handling
If a user tries to borrow or return a book with an invalid library_id, the system raises a ValueError.
Example:
python
Copy code
try:
    library.borrow_book("9999", "1984")  # Invalid ID
except ValueError as e:
    print(e)  # Outputs: "No user with Library ID 9999"
Future Enhancements
Add functionality for managing book inventory (e.g., tracking availability, adding/removing books).
Implement a search feature for books and users.
Enhance the CLI with a menu-based interface for better usability.
Store user and book data persistently using files or a database.
Contributing
Fork this repository.
Create a feature branch: git checkout -b feature-name.
Commit your changes: git commit -m 'Add feature'.
Push to the branch: git push origin feature-name.
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Created by [TEVIN BARRIOS]
