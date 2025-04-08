class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        """ print all the details """
        pass
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self