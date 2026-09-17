
class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def salary_raise(self,new_salary):
        self.salary=self.salary+new_salary
        print("New salary raise successfully",self.salary)
    def display(self):
        print("Employee name",self.name)
        print("Employee Id is :",self.id)
        print("Employee updated salary is ",self.salary)
name=input("Enter employee name is :")
id=int(input("Enter employee id is :"))
salary=int(input("Enter employee salary is :"))
new_salary=int(input("Enter raise salary is :"))
e=Employee(name,id,salary)
e.salary_raise(new_salary)
e.display()