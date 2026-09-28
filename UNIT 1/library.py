class library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def show_books(self):
        for book in self.books:
            print(book.show_book_info())

    def show_users(self):
        for user in self.users:
            print(user.show_user_info())

    def borrow_book(self, id_book, id_user):
        book = next((b for b in self.books if b.id_book == id_book), None)
        
        if book:
            if book.available:
                book.available = False
                print(f"Success: Book '{book.name}' has been borrowed by user {id_user}.")
            else:
                print(f"Error: Book '{book.name}' is already borrowed and cannot be borrowed again.")
        else:
            print("Error: Book not found in the system.")

    def return_book(self, id_book):
        book = next((b for b in self.books if b.id_book == id_book), None)
        
        if book:
            if not book.available:
                book.available = True
                print(f"Success: Book '{book.name}' has been returned and is available again.")
            else:
                print(f"Notice: Book '{book.name}' was already available.")
        else:
            print("Error: Book not found in the system.")