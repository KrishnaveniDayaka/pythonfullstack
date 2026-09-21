#A getter is used to read/access a private value.
class Student:
    def __init__(self, marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks
s = Student(90)
print(s.get_marks())