# flake8: noqa
import collections
class Library:
    def __init__(self):
        self.books= {}

    
    def add_book(self,title,quantity):
        self.title = title
        
        self.quantity = quantity


        
        self.books[title] = self.books.get(title,0) +1 

        

    def borrow_book(self,title):
        value = self.books.get(title)
        if value > 0:
            self.books[title] = self.books.get(title) -1

    def return_book(self,title):
        value = self.books.get(title)
        if value >=0 :
            self.books[title] = self.books.get(title)+1

obj_library = Library()

obj_library.add_book("DS",1)
obj_library.add_book("DS",2)
obj_library.add_book("KS",1)
print(obj_library.books)







