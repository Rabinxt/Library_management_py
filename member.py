from book import Book

class Member():
    def __init__(self,member_id,member_name):
        self.member_id=member_id
        self.member_name=member_name
        self.borrowed_books=[]
    
    def borrow(self, book):
        if book.is_book_available():
            self.borrowed_books.append(book)
            book.mark_borrowed()
            print(f"{self.member_name} successfully borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")

    def return_book(self, book):
        """
        Allows the member to return a borrowed book.
    
        :param book: The book object to be returned.
        """
        pass
    
    def list_borrowed_books(self):
        """
        Lists all books currently borrowed by the member.
        """
        pass
    
    def has_borrowed(self):
        """
        Checks if the member has borrowed any books.
    
        :return: True if the member has borrowed books, False otherwise.
        """
        pass
    
    def update_details(self, new_name):
        """
        Updates the member's personal details.
    
        :param new_name: New name for the member.
        """
        pass
    
