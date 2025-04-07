books = {
    1: {"title": "1984", "author": "George Orwell", "is_available": True},
    2: {"title": "To Kill a Mockingbird", "author": "Harper Lee", "is_available": True}
}

class Book():
    def __init__(self,title,author,book_id):
        self.title=title
        self.author=author
        self.book_id=book_id
        self.is_available=True

    def __str__(self):
        return f"Title:{self.title}, Author:{self.author},ID:{self.book_id},Status:{self.is_available}"
    
    def add_book(self):
         
        new_book_id = self.book_id
        books[new_book_id] = {
            "title": self.title,
            "author": self.author,
            "is_available": self.is_available
        }
        print(f"Book added: {self.title} by {self.author} (ID: {self.book_id})")
    
    
    def mark_borrowed(self):
        if self.is_available:
            self.is_available=False
            books[self.book_id]["is_available"]=False
            print(f"{self.title} is borrowed")
        else:
            print(f"'{self.title}' is already borrowed.")


    def mark_returned(self):
        if not self.is_available:
            self.is_available=True 
            books[self.book_id]["is_available"] = True
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")


    def is_book_available(self):
        return self.is_available
    
    
    def book_update(self,new_title,new_author):
        self.title=new_title
        self.author=new_author 
        books[self.book_id]["title"] = new_title
        books[self.book_id]["author"] = new_author
        print(f"Book details updated: {self.title} by {self.author}.")
