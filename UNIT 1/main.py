from books import book
from users_Rodriguez_Jose import user
from library import library

# Instantiate the library with a variable name different from the class name
my_library = library()

book1 = book(1, "The Great Gatsby", "F. Scott Fitzgerald", "Scribner")
book2 = book(2, "To Kill a Mockingbird", "Harper Lee", "J.B. Lippincott & Co.")
user1 = user(1, "John Doe")

# Requirement 1: The system must allow register books.
print("--- 1. Registering Books ---")
my_library.add_book(book1)
my_library.add_book(book2)
my_library.show_books()

# Requirement 2: The system must allow register users.
print("\n--- 2. Registering Users ---")
my_library.add_user(user1)
my_library.show_users()

# Requirement 3: The system must allow a book to be borrowed by a user.
print("\n--- 3. Borrowing a book ---")
my_library.borrow_book(1, 1)

# Requirement 4: A book that has already been borrowed cannot be borrowed again.
print("\n--- 4. Trying to borrow an already borrowed book ---")
my_library.borrow_book(1, 1)

# Requirement 5: The system must allow a book to be returned.
print("\n--- 5. Returning the book ---")
my_library.return_book(1)

print("\n--- Final catalog status ---")
my_library.show_books()