
from book import Book
from member import Member

# Create books
book1 = Book("1984", "George Orwell", 1)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 2)

# Create a member
member1 = Member(1, "John Doe")
# Borrow a book (pass the Book instance, not the ID)
member1.borrow(book1)