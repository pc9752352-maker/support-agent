class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self): #dunder method
        status = "Available" if self.is_available else "Borrowed"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - [{status}]"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        book_list = ", ".join([b.title for b in self.borrowed_books]) or "No books"
        return f"Member: {self.name} (ID: {self.member_id}) | Borrowed: {book_list}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Added: {new_book.title}")

    def register_member(self, name, member_id):
        new_member = Member(name, member_id)
        self.members.append(new_member)
        print(f"Registered Member: {new_member.name}")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def issue_book(self, isbn, member_id):
        book = self.find_book(isbn)
        member = self.find_member(member_id)

        if not book:
            print("Error: Book not found.")
        elif not member:
            print("Error: Member not registered.")
        elif not book.is_available:
            print(f"Error: '{book.title}' is already borrowed.")
        else:
            book.is_available = False
            member.borrowed_books.append(book)
            print(f"Success: '{book.title}' issued to {member.name}.")

    def return_book(self, isbn, member_id):
        member = self.find_member(member_id)
        if member:
            for book in member.borrowed_books:
                if book.isbn == isbn:
                    book.is_available = True
                    member.borrowed_books.remove(book)
                    print(f"Success: '{book.title}' returned by {member.name}.")
                    return
        print("Error: Return failed. Check ISBN or Member ID.")

# --- Demonstration ---
my_library = Library()

# 1. Setup Data
my_library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "123")
my_library.add_book("1984", "George Orwell", "456")
my_library.register_member("Alice", "M001")

# 2. Process a Borrowing Transaction
print("\n--- Transaction Test ---")
my_library.issue_book("123", "M001")

# 3. Check Status
print("\n--- Current Status ---")
print(my_library.find_book("123"))
print(my_library.find_member("M001"))