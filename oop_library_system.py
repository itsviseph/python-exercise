# creating a oop library
# creating a book class


# -----------------------------
# Book class
# -----------------------------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow_book(self):
        if self.is_borrowed:
            print(f"{self.title} is not available")
            return False
        else:
            self.is_borrowed = True
            print(f"{self.title} is borrowed successfully")
            return True

    def return_book(self):
        if not self.is_borrowed:
            print(f"{self.title} was not borrowed")
            return False
        else:
            self.is_borrowed = False
            print(f"{self.title} is returned successfully")
            return True


# -----------------------------
# User class
# -----------------------------
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def add_book(self, book):
        self.borrowed_books.append(book)

    def remove_book(self, book):
        self.borrowed_books.remove(book)
