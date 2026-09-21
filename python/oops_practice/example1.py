
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Person name is {self.name} And Person Age is {self.age}")
name=input("Enter a Person name:")
age=int(input("Enter a Person age:"))
p=Person(name,age)
p.display()