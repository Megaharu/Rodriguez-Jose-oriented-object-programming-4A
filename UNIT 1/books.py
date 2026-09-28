class book:
    def __init__(self, id_book, name, author, editorial):
        self.id_book = id_book
        self.name = name
        self.author = author
        self.editorial = editorial
        self.available = True
    def show_book_info(self):
        return f"Book ID: {self.id_book}, Name: {self.name}, Author: {self.author}, Editorial: {self.editorial}, Available: {self.available}"