
#What is Class ?
#A class is a blueprint or template used to create objects. It defines the data and behavior that objects can have.

class Student:
    name="krishna"#variables/data/properties
    age=21
    def check(self):#behaviours/methods  check() is a method because it is a function defined inside the class.
        pass

print(Student)
print(type(Student)) #It gives type of Student
print(id(Student)) #It gives address of Student class
print(Student.name)
print(Student.age)