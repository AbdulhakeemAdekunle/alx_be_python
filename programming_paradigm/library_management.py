class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        _is_checked_out = False
    
    def check_out(self):
        self._is_checked_out = True
    def return_book(self):
        self._is_checked_out = False
    def is_checked_out(self):
        return self._is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        self.title = title
        for book in self._books:
            if self.title == title and not Book.is_checked_out():
                Book.check_out()
                return f'"{title}" has been checked out.'
            
            return f'Book "{title}" is not available.'

    def return_book(self, title):
        for book in self._books:
            if self.title == title and Book.is_checked_out():
                Book.return_book()
                return f'Book "{title}" has been returned.'
        return f'Book "{title}" is not checked out.' 

    def list_available_books(self):
        available_books = [self.title for book in self._books is not Book.is_checked_out()]