
class Circle:
    
    def __init__(self,r):
        self.r=r
        self.pie=3.14
    def area(self):
        result=self.pie*self.r*self.r
        print(f"Area of circle is :{result}")
    def circumstance(self):
        c1=self.pie*2*self.r
        print("Circumstance of circle is :",c1)
r=int(input("Enter r value :"))
c=Circle(r)
c.area()
c.circumstance()