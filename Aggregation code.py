#Aggregation
class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

# --- Execution ---
if __name__ == "__main__":
    independent_book = Book("The Hobbit")
    my_library = Library()
    my_library.add_book(independent_book)
    print(f"Added '{independent_book.title}' to the library.")

    del my_library  
    print(f"Library closed, but '{independent_book.title}' still exists.")
