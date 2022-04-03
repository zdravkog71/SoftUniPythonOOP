class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        #self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def find_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                return book
        return f"No book with title {book_title}"