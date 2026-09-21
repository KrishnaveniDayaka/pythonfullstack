
#A method is a function defined inside a class that is used to perform
#  an operation on an object or access/manipulate the object's data.
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Student name is {self.name} and student Age is {self.age}")
s1=Student("krishna",21)
s1.display()
#Here Student is class
#__init__ is constructor
#self.name,self.age are instance variables
#display is method
#s1 is object for Student class