# creating a oop library
# creating a book class


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow_book(self):
        if self.is_borrowed:
            print(f"{self.title} is not available")
        else:
            self.is_borrowed = True
            print(f"{self.title} is borrowed successfully")

    def return_book(self):
        if not self.is_borrowed:
            print(f"{self.title} was not borrowed")
        else:
            self.is_borrowed = False
            print(f"{self.title} is returned successfully")


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
