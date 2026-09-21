class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
s = Student("Krishna", 90)
print(s.name)
print(s.marks)
s.marks = 95
print(s.marks)