class Student:
    def __init__(self):
        self._marks = 90   # protected variable
    def show_marks(self):
        print(self._marks)
s = Student()
s.show_marks()
print(s._marks)