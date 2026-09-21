class Book:
    def __init__(self, pages):
        self.pages = pages
    def __add__(self, other):
        return Book(self.pages + other.pages)
    def __sub__(self, other):
        return Book(self.pages - other.pages)
    def __mul__(self, other):
        return Book(self.pages * other.pages)
    def __gt__(self, other):
        return self.pages > other.pages
    def __eq__(self, other):
        return self.pages == other.pages
    def __str__(self):
        return str(self.pages)
b1 = Book(100)
b2 = Book(50)
print(b1 + b2)
print(b1 - b2)
print(b1 * b2)
print(b1 > b2)
print(b1 == b2)