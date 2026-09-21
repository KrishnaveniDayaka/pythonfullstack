
# ============================================================
# PYTHON BASICS - CODING PRACTICE
# ============================================================


# ============================================================
# 1. COMMENTS
# ============================================================

# Definition:
# A comment is a line of text in a Python program that is
# ignored by the Python interpreter.
# Comments are used to explain code, improve readability,
# add notes, and temporarily disable code during testing.

# This is a single-line comment.

print("Hello Python")


# ============================================================
# 2. SINGLE-LINE COMMENT
# ============================================================

# Definition:
# A single-line comment starts with the # symbol.

# Printing a welcome message
print("Welcome to Python")


# ============================================================
# 3. MULTIPLE SINGLE-LINE COMMENTS
# ============================================================

# Definition:
# Multiple single-line comments can be written using #
# on separate lines.

# Student Information
# Name: Krishna
# Course: Python Full Stack
# Batch: PFS

print("Student Registered")


# ============================================================
# 4. MULTI-LINE TEXT / TRIPLE-QUOTED STRING
# ============================================================

# Definition:
# Python does not have a special multi-line comment syntax.
# Triple-quoted strings can be used for multi-line text.
# When placed at the beginning of a module, class, or function,
# they can serve as documentation strings (docstrings).

"""
This is a multi-line text block.
It can contain multiple lines.
"""

print("Python")


# ============================================================
# 5. SWAPPING TWO VARIABLES
# ============================================================

# Definition:
# Swapping means exchanging the values of two variables.

a = 10
b = 20

print("Before swapping:", a, b)

a, b = b, a

print("After swapping:", a, b)


# ============================================================
# 6. SWAPPING USING THIRD VARIABLE
# ============================================================

# Definition:
# We can swap two variables by using a third temporary variable.

a = 10
b = 20

temp = a
a = b
b = temp

print(a, b)


# ============================================================
# 7. SWAPPING WITHOUT THIRD VARIABLE
#    USING ARITHMETIC
# ============================================================

# Definition:
# Two variables can be swapped without a third variable
# by using arithmetic operations.

a = 10
b = 20

a = a + b
b = a - b
a = a - b

print(a, b)


# ============================================================
# 8. PYTHONIC SWAPPING
# ============================================================

# Definition:
# Python provides a simple way to swap two variables
# using multiple assignment (tuple unpacking).

a = 10
b = 20

a, b = b, a

print(a, b)

# This is the recommended and commonly used method in Python.


# ============================================================
# 9. VARIABLES
# ============================================================

# Definition:
# A variable is a name that refers (binds) to an object (value).

# Syntax:
# variable_name = value

age = 22
name = "Krishna"
percentage = 95.5

print(age)
print(name)
print(percentage)


# ============================================================
# 10. VARIABLE REFERENCES
# ============================================================

# Definition:
# In Python, a variable name refers to an object in memory.

age = 22

print(age)

# age -> variable/name
# 22  -> integer object


# ============================================================
# 11. CHECKING VARIABLE TYPE
# ============================================================

# Definition:
# type() is a built-in function used to check
# the data type of an object.

age = 22

print(type(age))


# ============================================================
# 12. DATA TYPES
# ============================================================

# Definition:
# A data type specifies the type of value stored in a variable.
# Python automatically determines the data type based
# on the assigned value.

a = 10

print(type(a))


# ============================================================
# 13. STRING - str
# ============================================================

# Definition:
# A string is a sequence of characters enclosed in quotes.
# Strings are immutable.

name = "Krishna"

print(name)
print(type(name))


# ============================================================
# 14. STRING INDEXING
# ============================================================

# Definition:
# Indexing is used to access individual characters.
# String indexing starts from 0.

name = "Python"

print(name[0])
print(name[1])
print(name[2])


# ============================================================
# 15. STRING PROPERTIES
# ============================================================

# Definition:
# Strings:
# - Store text
# - Are immutable
# - Are ordered
# - Support indexing

name = "Python"

print(name)
print(name[0])

# name[0] = "J"
# This would give TypeError because strings are immutable.


# ============================================================
# 16. INTEGER - int
# ============================================================

# Definition:
# int represents whole numbers such as positive numbers,
# negative numbers, and zero.

age = 22
marks = 500
temperature = -10

print(age)
print(marks)
print(temperature)

print(type(age))


# ============================================================
# 17. FLOAT - float
# ============================================================

# Definition:
# float represents decimal numbers.

percentage = 97.5
temperature = 40.5
salary = 25000.75

print(percentage)
print(temperature)
print(salary)

print(type(percentage))


# ============================================================
# 18. COMPLEX - complex
# ============================================================

# Definition:
# A complex number contains a real part and an imaginary part.
# Python uses j to represent the imaginary part.

z = 4 + 5j

print(z)
print(type(z))


# ============================================================
# 19. REAL PART OF COMPLEX NUMBER
# ============================================================

# Definition:
# The real attribute returns the real part of a complex number.

z = 4 + 5j

print(z.real)


# ============================================================
# 20. IMAGINARY PART OF COMPLEX NUMBER
# ============================================================

# Definition:
# The imag attribute returns the imaginary part
# of a complex number.

z = 4 + 5j

print(z.imag)


# ============================================================
# 21. LIST
# ============================================================

# Definition:
# A list stores multiple values in a single variable.
# Lists are represented using square brackets [].

cart = ["Shoes", "Shirt", "Watch"]

print(cart)


# ============================================================
# 22. LIST INDEXING
# ============================================================

# Definition:
# List indexing is used to access elements.
# List indexing starts from 0.

cart = ["Shoes", "Shirt", "Watch"]

print(cart[0])
print(cart[1])
print(cart[2])


# ============================================================
# 23. LIST IS MUTABLE
# ============================================================

# Definition:
# A list is mutable, which means its contents can be changed
# after the list is created.

numbers = [10, 20, 30]

print(numbers)

numbers.append(40)

print(numbers)


# ============================================================
# 24. LIST ALLOWS DUPLICATES
# ============================================================

# Definition:
# A list can contain duplicate values.

numbers = [10, 20, 10, 30, 20]

print(numbers)


# ============================================================
# 25. LIST CAN STORE DIFFERENT DATA TYPES
# ============================================================

# Definition:
# A list can store values of different data types.

student = ["Krishna", 22, 95.5, True]

print(student)


# ============================================================
# 26. TUPLE
# ============================================================

# Definition:
# A tuple is an ordered collection of items enclosed
# in parentheses ().

dimensions = (10, 30, 40, 50)

print(dimensions)


# ============================================================
# 27. TUPLE INDEXING
# ============================================================

# Definition:
# Tuple indexing starts from 0 and is used to access elements.

colors = ("Red", "Blue", "Green")

print(colors[0])
print(colors[1])
print(colors[2])


# ============================================================
# 28. TUPLE IS IMMUTABLE
# ============================================================

# Definition:
# A tuple is immutable, which means its elements cannot
# be changed after creation.

numbers = (10, 20, 30)

print(numbers)

# numbers[0] = 100
# This produces TypeError because tuple is immutable.


# ============================================================
# 29. SINGLE-ITEM TUPLE
# ============================================================

# Definition:
# A single-item tuple must contain a comma.

student = ("Raju",)

print(student)
print(type(student))


# ============================================================
# 30. WITHOUT COMMA - NOT A TUPLE
# ============================================================

# Definition:
# Parentheses alone do not create a tuple.
# The comma tells Python that it is a tuple.

student = ("Raju")

print(student)
print(type(student))

# Output:
# Raju
# <class 'str'>


# ============================================================
# 31. SINGLE INTEGER TUPLE
# ============================================================

# Definition:
# A tuple containing one integer requires a comma.

number = (10,)

print(number)
print(type(number))


# ============================================================
# 32. LIST VS TUPLE
# ============================================================

# Definition:
# List is mutable and uses [].
# Tuple is immutable and uses ().

my_list = [10, 20, 30]
my_tuple = (10, 20, 30)

print(my_list)
print(my_tuple)

# List can be modified
my_list[0] = 100

print(my_list)

# Tuple cannot be modified
# my_tuple[0] = 100
# TypeError


# ============================================================
# 33. RANGE
# ============================================================

# Definition:
# A range object generates a sequence of numbers.
# It is commonly used with loops.

numbers = range(5)

print(numbers)


# ============================================================
# 34. RANGE WITH ONE ARGUMENT
# ============================================================

# Definition:
# range(stop) generates numbers from 0 up to,
# but not including, stop.

numbers = range(5)

print(list(numbers))

# Output:
# [0, 1, 2, 3, 4]


# ============================================================
# 35. RANGE WITH TWO ARGUMENTS
# ============================================================

# Definition:
# range(start, stop) generates numbers from start
# up to, but not including, stop.

numbers = range(2, 8)

print(list(numbers))

# Output:
# [2, 3, 4, 5, 6, 7]


# ============================================================
# 36. RANGE WITH THREE ARGUMENTS
# ============================================================

# Definition:
# range(start, stop, step) generates numbers starting
# from start and increases by step.

numbers = range(0, 10, 2)

print(list(numbers))

# Output:
# [0, 2, 4, 6, 8]


# ============================================================
# 37. RANGE WITH NEGATIVE STEP
# ============================================================

# Definition:
# A negative step generates numbers in decreasing order.

numbers = range(10, 0, -2)

print(list(numbers))

# Output:
# [10, 8, 6, 4, 2]


# ============================================================
# 38. TYPE CHECKING
# ============================================================

# Definition:
# type() returns the data type of an object.

name = "Krishna"
age = 22
percentage = 97.5
numbers = [10, 20, 30]
values = (10, 20, 30)

print(type(name))
print(type(age))
print(type(percentage))
print(type(numbers))
print(type(values))


# ============================================================
# 39. COMPLETE DATA TYPES PRACTICE
# ============================================================

# Definition:
# Python has different built-in data types for storing
# different kinds of values.

name = "Krishna"             # str
age = 22                     # int
salary = 25000.50           # float
complex_number = 4 + 5j     # complex

student_list = [10, 20, 30] # list
student_tuple = (10, 20, 30) # tuple
student_range = range(5)    # range

student_dict = {"name": "Krishna"}  # dict
student_set = {10, 20, 30}          # set
student_status = True               # bool
student_value = None                # NoneType

print(type(name))
print(type(age))
print(type(salary))
print(type(complex_number))
print(type(student_list))
print(type(student_tuple))
print(type(student_range))
print(type(student_dict))
print(type(student_set))
print(type(student_status))
print(type(student_value))


# ============================================================
# 40. FINAL COMBINATION PROGRAM
# ============================================================

# Definition:
# This program combines variables, data types, operators,
# strings, lists, tuples, range, and type().

student_name = "Krishna"
age = 22
marks = 450
subjects = 5

average = marks / subjects

subjects_list = ["Python", "SQL", "HTML", "CSS", "JavaScript"]

student_details = (student_name, age, marks)

print("Student Name:", student_name)
print("Age:", age)
print("Marks:", marks)
print("Subjects:", subjects)
print("Average:", average)

print("Subjects List:", subjects_list)
print("Student Details:", student_details)

print("Name Type:", type(student_name))
print("Age Type:", type(age))
print("Marks Type:", type(marks))
print("Average Type:", type(average))