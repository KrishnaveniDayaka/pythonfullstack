

# ============================================================
# PYTHON BASICS - CODING PRACTICE
# ============================================================


# ============================================================
# 1. SIMPLE PYTHON PROGRAM
# ============================================================

# Definition:
# A Python program is a set of instructions written using Python syntax.

print("Hello World")


# ============================================================
# 2. PRINT FUNCTION
# ============================================================

# Definition:
# print() is a built-in Python function used to display output on the console.

print("Welcome to Python")
print(10)
print(10 + 20)


# ============================================================
# 3. STATEMENT
# ============================================================

# Definition:
# A statement is an instruction that Python can execute.

a = 10
b = 20
print(a + b)


# ============================================================
# 4. TOKENS
# ============================================================

# Definition:
# A token is the smallest meaningful unit of a Python program.

a = 10

# Tokens in the above statement:
# a  -> Identifier
# =  -> Operator
# 10 -> Literal


# ============================================================
# 5. KEYWORDS
# ============================================================

# Definition:
# Keywords are reserved words in Python that have predefined meanings.
# They cannot be used as variable names.

if True:
    print("This is a keyword example")

# Other examples:
# if, else, for, while, class, def, return, break,
# continue, True, False, None, try, except


# ============================================================
# 6. IDENTIFIERS
# ============================================================

# Definition:
# Identifiers are names given by the programmer to variables,
# functions, classes, modules, etc.

student_name = "Krishna"
age = 22

print(student_name)
print(age)


# ============================================================
# 7. LITERALS
# ============================================================

# Definition:
# Literals are fixed values written directly in a Python program.

age = 22              # Integer literal
salary = 25000.50     # Float literal
name = "Krishna"      # String literal
is_student = True     # Boolean literal
value = None          # None literal

print(age)
print(salary)
print(name)
print(is_student)
print(value)


# ============================================================
# 8. OPERATORS
# ============================================================

# Definition:
# Operators are symbols or keywords used to perform operations on values.

a = 10
b = 3

# Arithmetic operators
print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a % b)    # Modulus
print(a // b)   # Floor division
print(a ** b)   # Exponentiation


# Comparison operators

# Definition:
# Comparison operators compare two values and return True or False.

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# Logical operators

# Definition:
# Logical operators are used to combine or reverse conditions.

print(a > 5 and b < 5)
print(a > 5 or b > 5)
print(not(a > 5))


# ============================================================
# 9. DELIMITERS / PUNCTUATORS
# ============================================================

# Definition:
# Delimiters are symbols used to organize and separate parts of Python code.

numbers = [10, 20, 30]

student = {
    "name": "Krishna",
    "age": 22
}

print(numbers)
print(student)


# ============================================================
# 10. VARIABLES
# ============================================================

# Definition:
# A variable is a name that refers to an object (value) in memory.

age = 22
name = "Krishna"

print(age)
print(name)


# ============================================================
# 11. TYPE OF VARIABLE / OBJECT
# ============================================================

# Definition:
# type() is a built-in function used to find the type of an object.

age = 22
name = "Krishna"
salary = 25000.50

print(type(age))
print(type(name))
print(type(salary))


# ============================================================
# 12. MULTIPLE ASSIGNMENT
# ============================================================

# Definition:
# Multiple assignment means assigning multiple values
# to multiple variables in a single statement.

a, b, c = 10, 20, 30

print(a)
print(b)
print(c)


# ============================================================
# 13. SAME VALUE TO MULTIPLE VARIABLES
# ============================================================

# Definition:
# Python allows one value to be assigned to multiple variables.

a = b = c = 100

print(a)
print(b)
print(c)


# ============================================================
# 14. REASSIGNMENT
# ============================================================

# Definition:
# Reassignment means assigning a new value to an existing variable.

a = 10

print(a)

a = 100

print(a)


# ============================================================
# 15. VARIABLE REFERENCE
# ============================================================

# Definition:
# In Python, a variable name refers to an object in memory.

a = 10

print(a)

# Here:
# a  -> variable/name
# 10 -> integer object


# ============================================================
# 16. IDENTITY OF OBJECT
# ============================================================

# Definition:
# id() returns the identity of an object.

a = 10

print(id(a))


# ============================================================
# 17. MUTABLE OBJECT
# ============================================================

# Definition:
# A mutable object can be changed after it is created.

numbers = [10, 20]

print(numbers)

numbers.append(30)

print(numbers)

# List contents changed.
# Therefore, list is mutable.


# ============================================================
# 18. DICTIONARY - MUTABLE
# ============================================================

# Definition:
# A dictionary is mutable because its contents can be changed.

student = {
    "name": "Krishna",
    "age": 22
}

print(student)

student["age"] = 23

print(student)


# ============================================================
# 19. SET - MUTABLE
# ============================================================

# Definition:
# A set is mutable because elements can be added or removed.

numbers = {10, 20, 30}

print(numbers)

numbers.add(40)

print(numbers)


# ============================================================
# 20. IMMUTABLE OBJECT
# ============================================================

# Definition:
# An immutable object cannot be changed after it is created.

name = "Python"

print(name)

name = name + " Programming"

print(name)

# A new string object is created.
# The original string object was not modified.


# ============================================================
# 21. TUPLE - IMMUTABLE
# ============================================================

# Definition:
# A tuple is immutable, so its elements cannot be changed after creation.

numbers = (10, 20, 30)

print(numbers)

# numbers[0] = 100
# This produces TypeError because tuple is immutable.


# ============================================================
# 22. VARIABLE NAMING RULES
# ============================================================

# Definition:
# Variable names must follow Python's identifier naming rules.

student_name = "Krishna"
age1 = 22
_marks = 95

print(student_name)
print(age1)
print(_marks)


# ============================================================
# 23. CASE SENSITIVE
# ============================================================

# Definition:
# Python is case-sensitive, so uppercase and lowercase names
# are treated as different identifiers.

age = 20
Age = 30
AGE = 40

print(age)
print(Age)
print(AGE)

# These are three different variables.


# ============================================================
# 24. MEANINGFUL VARIABLE NAMES
# ============================================================

# Definition:
# Meaningful variable names make code easier to understand and maintain.

student_name = "Krishna"
total_marks = 450
employee_salary = 30000

print(student_name)
print(total_marks)
print(employee_salary)


# ============================================================
# 25. INVALID VARIABLE NAMES
# ============================================================

# Variable names cannot start with a number.

# 2age = 22       # SyntaxError


# Spaces are not allowed in variable names.

# student name = "Krishna"    # SyntaxError


# Hyphen is not allowed in variable names.

# student-name = "Krishna"    # Not a valid variable name


# Keywords cannot be used as variable names.

# if = 10        # SyntaxError


# ============================================================
# 26. INTERACTIVE MODE
# ============================================================

# Definition:
# Interactive mode allows Python statements to be executed
# one at a time using the Python prompt >>>.

# Example:
#
# >>> print("Hello")
# Hello
#
# >>> 10 + 20
# 30
#
# >>> name = "Krishna"
# >>> print(name)
# Krishna


# ============================================================
# 27. SCRIPT MODE
# ============================================================

# Definition:
# Script mode means writing Python code in a .py file
# and executing the complete program.

# Example file:
#
# example.py
#
# print("Hello")
# a = 10
# b = 20
# print(a + b)

# Run from terminal:
#
# python example.py


# ============================================================
# 28. BYTECODE
# ============================================================

# Definition:
# Bytecode is an intermediate form of Python code generated
# after Python compiles the source code.

# Source code:
#
# print("Hello")
#
# .py
#   ↓
# Bytecode
#   ↓
# Python Virtual Machine (PVM)
#   ↓
# Execution


# ============================================================
# 29. PVM
# ============================================================

# Definition:
# PVM stands for Python Virtual Machine.
# It executes Python bytecode.

# Execution flow:
#
# Python Source Code
#        ↓
# Compiler
#        ↓
# Bytecode
#        ↓
# PVM
#        ↓
# Execution
#        ↓
# Output


# ============================================================
# 30. FINAL SMALL PRACTICE PROGRAM
# ============================================================

# Definition:
# This program combines variables, literals, operators,
# identifiers, print(), and statements.

student_name = "Krishna"
age = 22
marks = 450
total_subjects = 5

average = marks / total_subjects

print("Student Name:", student_name)
print("Age:", age)
print("Total Marks:", marks)
print("Average:", average)