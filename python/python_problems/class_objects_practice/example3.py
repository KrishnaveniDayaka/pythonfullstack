
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(f"Addition of two numbers is :{self.a+self.b}")
    def sub(self):
        print(f"Subtraction of two numbers is :{self.a-self.b}")
    def mul(self):
        print(f"Multiplication of  two numbers is :{self.a * self.b}")
    def div(self):
        print(f"Division of two numbers is :{self.a //self.b}")

a=int(input("enter a value:"))
b=int(input("Enter b value:"))
c=Calculator(a,b)
c.add()
c.sub()
c.mul()
c.div()