"""
OOP Library Management System

This project demonstrates basic Object-Oriented Programming concepts:
- Encapsulation
- Abstraction
- Composition
- Responsibility separation

Classes:
- Book: represents a book and manages its own availability
- User: represents a library user and tracks borrowed books
- Library: coordinates borrowing and returning of books
"""


# -----------------------------
# Book class
# -----------------------------
class Book:
    def __init__(self, title, author):
        # Book attributes
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow_book(self):
        """
        Attempt to borrow the book.
        Returns True if successful, False otherwise.
        """
        if self.is_borrowed:
            print(f'"{self.title}" is not available.')
            return False
        else:
            self.is_borrowed = True
            print(f'"{self.title}" has been borrowed.')
            return True

    def return_book(self):
        """
        Attempt to return the book.
        Returns True if successful, False otherwise.
        """
        if not self.is_borrowed:
            print(f'"{self.title}" was not borrowed.')
            return False
        else:
            self.is_borrowed = False
            print(f'"{self.title}" has been returned.')
            return True


# -----------------------------
# User class
# -----------------------------
class User:
    def __init__(self, name):
        # User attributes
        self.name = name
        self.borrowed_books = []

    def add_book(self, book):
        """Add a book to the user's borrowed list."""
        self.borrowed_books.append(book)

    def remove_book(self, book):
        """Remove a book from the user's borrowed list."""
        self.borrowed_books.remove(book)

    def list_borrowed_books(self):
        """Display all books currently borrowed by the user."""
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
        else:
            print(f"{self.name} has borrowed:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")


# -----------------------------
# Library class
# -----------------------------
class Library:
    def __init__(self, books):
        # Library stores all available books
        self.books = books

    def borrow_book(self, user, title):
        """
        Allow a user to borrow a book by title.
        """
        for book in self.books:
            if book.title == title:
                if book.borrow_book():
                    user.add_book(book)
                return
        print("Book not found in library.")

    def return_book(self, user, title):
        """
        Allow a user to return a borrowed book by title.
        """
        for book in user.borrowed_books:
            if book.title == title:
                if book.return_book():
                    user.remove_book(book)
                return
        print("This user does not have that book.")


# -----------------------------
# Example usage (basic test)
# -----------------------------
if __name__ == "__main__":
    # Create books
    book1 = Book("1984", "George Orwell")
    book2 = Book("The Alchemist", "Paulo Coelho")
    book3 = Book("Atomic Habits", "James Clear")

    # Create library with books
    library = Library([book1, book2, book3])

    # Create user
    user = User("Vishal")

    # Borrow books
    library.borrow_book(user, "1984")
    library.borrow_book(user, "Atomic Habits")

    # List borrowed books
    user.list_borrowed_books()

    # Return a book
    library.return_book(user, "1984")

    # List again
    user.list_borrowed_books()
