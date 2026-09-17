
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name :{self.name} , Age:{self.age}")
name=input("Enter a person name:")
age=int(input("enter a age of person:"))
p=Person(name,age)
p.display()