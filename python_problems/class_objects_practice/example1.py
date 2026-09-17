
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print(f"Area of rectangle is {self.length*self.width}")
    def per(self):
        print(f"Permeiter of rectangle is {2*(self.length+self.width)}")
length=int(input("Enter length:"))
width=int(input("Enter width:"))
r=Rectangle(length,width)
r.area()
r.per()