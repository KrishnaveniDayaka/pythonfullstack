
from abc import ABC, abstractmethod


# Base Abstract Class
class Person(ABC):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @abstractmethod
    def get_role(self):
        pass

    def get_details(self):
        return f"Name: {self._name}, Age: {self._age}, Role: {self.get_role()}"


# Student Class
class Student(Person):

    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self._student_id = student_id
        self._course = course

    def get_role(self):
        return "Student"

    def get_details(self):
        return (
            f"Name: {self._name}, Age: {self._age}, "
            f"Role: Student, ID: {self._student_id}, "
            f"Course: {self._course}"
        )


# Professor Class
class Professor(Person):

    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self._employee_id = employee_id
        self._department = department

    def get_role(self):
        return "Professor"

    def get_details(self):
        return (
            f"Name: {self._name}, Age: {self._age}, "
            f"Role: Professor, Employee ID: {self._employee_id}, "
            f"Department: {self._department}"
        )


# Admin Staff Class
class AdminStaff(Person):

    def __init__(self, name, age, staff_id, designation):
        super().__init__(name, age)
        self._staff_id = staff_id
        self._designation = designation

    def get_role(self):
        return "Admin Staff"

    def get_details(self):
        return (
            f"Name: {self._name}, Age: {self._age}, "
            f"Role: Admin Staff, Staff ID: {self._staff_id}, "
            f"Designation: {self._designation}"
        )


# University Class
class University:

    university_name = "Codegnan University"

    def __init__(self):
        self.__people = []

    def add_person(self, person: Person):
        self.__people.append(person)

    def display_all(self):
        if not self.__people:
            print("No people registered.")
        else:
            for person in self.__people:
                print(person.get_details())


# Main Program
print("Welcome to University Management System")
print("University:", University.university_name)

u = University()

while True:

    print("\n----- MENU -----")
    print("1. Register Student")
    print("2. Register Professor")
    print("3. Register Admin Staff")
    print("4. Display All People")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        student_id = input("Enter student ID: ")
        course = input("Enter course: ")

        student = Student(name, age, student_id, course)
        u.add_person(student)

        print("Student registered successfully!")

    elif choice == "2":

        name = input("Enter professor name: ")
        age = int(input("Enter age: "))
        employee_id = input("Enter employee ID: ")
        department = input("Enter department: ")

        professor = Professor(
            name, age, employee_id, department
        )

        u.add_person(professor)

        print("Professor registered successfully!")

    elif choice == "3":

        name = input("Enter staff name: ")
        age = int(input("Enter age: "))
        staff_id = input("Enter staff ID: ")
        designation = input("Enter designation: ")

        staff = AdminStaff(
            name, age, staff_id, designation
        )

        u.add_person(staff)

        print("Admin staff registered successfully!")

    elif choice == "4":

        print("\n--- Registered People ---")
        u.display_all()

    elif choice == "0":

        print("Thank you! Exiting...")
        break

    else:

        print("Invalid choice!")