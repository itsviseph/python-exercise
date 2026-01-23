class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow_book(self):
        if self.is_borrowed:
            print("the book is not available")
            return False

        else:
            self.is_borrowed = True
            print("the book has been borrowed")
            return True

    def return_book(self):
        if not self.is_borrowed:
            print("the book is not borrowed to be returned ")
            return False

        else:
            self.is_borrowed = False
            print("the book has been returned")
            return True


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def add_book(self, book):
        self.borrowed_books.append(book)

    def remove_book(self, book):
        self.borrowed_books.remove(book)


class Library:
    def __init__(self, books):
        self.books = books

    def borrow_books(self, user, title):
        for book in self.books:
            if book.title == title:
                success = book.borrow_book()
                if success:
                    user.add_book(book)
                    return
        print("Book not found.")

    def return_books(self, user, title):
        for book in user.borrowed_books:
            if book.title == title:
                success = book.return_book()
                if success:
                    user.remove_book(book)
                    return
        print("this user doe not have the book")
