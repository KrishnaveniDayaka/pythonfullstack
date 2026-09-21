class Student:
    def __init__(self):
        self.__marks = 90
    def show_marks(self):
        print(self.__marks)
s = Student()
s.show_marks()
# print(s.__marks)   # AttributeError