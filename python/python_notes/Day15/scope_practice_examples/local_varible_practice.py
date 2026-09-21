
class Student:
    college='lbrce'
    def name(self):
        age=21   #Local Variables
        dept='cse'
        print(age,dept)
s=Student()
s.name()
print()
print(age) #accessing local variable outside the method we get error