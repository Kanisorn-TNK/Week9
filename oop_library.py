class Library:
    def __init__(self):
        self.books = {}

    def add_books(self):
        Adds = int(input("How many books do you want to add? : "))
        for i in range(Adds):
            book_name = input("Enter book name: ")
            book_auther = input("Enter auther name : ")
            book_pages = int(input("Enter book page : "))
            book_price = int(input("Enter book price : "))
            self.books[book_name] = (book_auther, book_pages, book_price)

    def show_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("-----Books in the library-----")
            for book_name, book_info in self.books.items():
                book_auther, book_pages, book_price = book_info
                print(f"Name: {book_name} | Auther: {book_auther} | Total page: {book_pages} | Price: {book_price}")

    def find_book(self):
        book_name = input("Enter book name to find : ")
        if book_name in self.books:
            book_auther, book_pages, book_price = self.books[book_name]
            print(f"Book found ---> Name: {book_name}, Auther: {book_auther}, Total page: {book_pages}, Price: {book_price}\n")
        else:
            print("Book not found.")

my_library = Library()

my_library.add_books()
my_library.show_books()
my_library.find_book()
