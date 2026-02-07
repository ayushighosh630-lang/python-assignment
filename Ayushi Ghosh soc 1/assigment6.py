class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(book)
        else:
            print("No books in the library.")


library = Library()
library.add_book("The Alchemist")
library.add_book("To Kill a Mockingbird")
library.add_book("1984")
library.display_books()