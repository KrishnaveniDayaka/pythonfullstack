
#A class method is a method that operates on class-level data and receives 
#the class itself as its first parameter, conventionally named cls.
class Student:
    college = "LBRCE"
    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college
print(Student.college)        
Student.change_college("Codegnan")
print(Student.college)
