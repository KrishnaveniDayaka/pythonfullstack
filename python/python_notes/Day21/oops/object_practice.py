#what is object?
# An object is an instance of a class.
# An object is created from a class and represents a real-world
# entity. It contains data and can access the behavior defined
# by the class.

class Student:
    name="krishna" #class Attributes/properties/variables
    age=21
    def check(self):#behaviours/methods  check() is a method because it is a function defined inside the class.
        pass
s1=Student() #I create object for student class
print(s1.name)
print(type(s1))
print(id(s1))
