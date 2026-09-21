
#An instance method is a method that operates on the
#instance (object) data and takes self as its first parameter.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
s1 = Student("Krishna", 90)
s1.display()