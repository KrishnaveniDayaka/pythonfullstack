
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self,length,width):
        print( self.length * self.width)
    def perimeter(self,length,width):
        print( 2 *(self.length+self.width))
length=float(input("Enter  length:"))
width=float(input("Enter width:"))
r=Rectangle(length,width)
r.area(length,width)
r.perimeter(length,width)
