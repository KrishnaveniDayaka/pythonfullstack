#A setter is used to change/update a private value.
class Student:
    def __init__(self, marks):
        self.__marks = marks
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated")
        else:
            print("Invalid marks")
    def get_marks(self):
        return self.__marks
s = Student(80)
print(s.get_marks())
s.set_marks(95)
print(s.get_marks())