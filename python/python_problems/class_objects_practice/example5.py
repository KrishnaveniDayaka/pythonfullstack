
class Student:
    def __init__(self,name,rollno,python,english,maths):
        self.name=name
        self.rollno=rollno
        self.python=python
        self.english=english
        self.maths=maths

    def display(self):
        print(f"Student name is {self.name} , Student rollno is {self.rollno} ")
    def average(self):
            avg=(self.python+self.english+self.maths)/3
            print("Average marks are :",avg)
name=input("Enter name:")
rollno=int(input("Enter roll no :"))
python=int(input('Enter python marks:'))
english=int(input("Enter english marks:"))
maths=int(input("Enter maths marks:"))
s=Student(name,rollno,python,english,maths)
s.average()
s.display()