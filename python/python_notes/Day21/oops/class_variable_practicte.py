
#what is class variable in python?
#A class variable is created directly inside the class, but outside methods.
#Class Variable
 #     ↓
#అందరికీ common information


class Student:
    college='Lbrce'     #This is class variable
    highest_degree='Btech'  #This is class variable inside class and outside init method 

    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        print(f"My name is {self.name} and My age is {self.age} ")
        print(Student.college)  #we can access class variable inside method using class name
        print(Student.highest_degree)
s1=Student('krishna',21)
s2=Student('kittu',20)






