class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_book_info(self):
        return f"{self.title} by {self.author}"

class BookPrinter:
    def print_book(self, book):
        print(book.get_book_info())

book1 = Book("Harry Potter","J K Rowling")
printer = BookPrinter()
printer.print_book(book1)