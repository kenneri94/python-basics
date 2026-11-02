# OOP

# properties + functions

# class template

# book, author,title, isbn, price

class Book:

    def __init__(self, author, title, isbn, price):
        self.author = author
        self.title = title
        self.isbn = isbn
        self.price = price

    def print_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("ISBN:", self.isbn)
        print("Price:", self.price)
        print("-----------")

    def apply_discount(self, discount):
        self.price = self.price * (1-discount/100)
        print("New price is:",self.price)


b1=Book("the river between","Kennedy otieno","ISBN4000", 400)