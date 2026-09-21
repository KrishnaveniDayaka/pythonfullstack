
# ============================================================
# PYTHON DATA TYPES - CODING PRACTICE
# SET, DICTIONARY, BOOLEAN, NONE, TYPE CASTING
# ============================================================


# ============================================================
# 1. SET
# ============================================================

# Definition:
# A set is a built-in Python data type used to store unique elements.
# Set does not allow duplicate values.
# Set is mutable.
# Set is unordered and does not support indexing.
# Set is represented using curly braces {}.

student_ids = {101, 102, 103, 104}

print(student_ids)
print(type(student_ids))


# ============================================================
# 2. SET DOES NOT ALLOW DUPLICATES
# ============================================================

# Definition:
# A set automatically removes duplicate values.

student_ids = {101, 102, 103, 101, 102}

print(student_ids)

# Output:
# {101, 102, 103}


# ============================================================
# 3. SET IS MUTABLE
# ============================================================

# Definition:
# Mutable means we can add or remove elements
# after creating the object.

fruits = {"Apple", "Mango"}

print(fruits)

fruits.add("Orange")

print(fruits)


# ============================================================
# 4. ADD ELEMENT TO SET
# ============================================================

# Definition:
# add() is used to add one element to a set.

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)


# ============================================================
# 5. REMOVE ELEMENT FROM SET
# ============================================================

# Definition:
# remove() is used to remove an element from a set.
# It raises KeyError if the element does not exist.

numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)


# ============================================================
# 6. DISCARD ELEMENT FROM SET
# ============================================================

# Definition:
# discard() removes an element from a set.
# Unlike remove(), discard() does not raise an error
# if the element does not exist.

numbers = {10, 20, 30}

numbers.discard(20)
numbers.discard(100)

print(numbers)


# ============================================================
# 7. EMPTY SET
# ============================================================

# Definition:
# set() is used to create an empty set.
# {} creates an empty dictionary, not an empty set.

s = set()

print(s)
print(type(s))


# ============================================================
# 8. EMPTY DICTIONARY
# ============================================================

# Definition:
# {} creates an empty dictionary.

d = {}

print(d)
print(type(d))


# ============================================================
# 9. SET DOES NOT SUPPORT INDEXING
# ============================================================

# Definition:
# Sets are unordered, so they do not have fixed positions
# and cannot be accessed using indexes.

numbers = {10, 20, 30}

print(numbers)

# print(numbers[0])
# TypeError: 'set' object is not subscriptable


# ============================================================
# 10. SET CAN STORE DIFFERENT IMMUTABLE DATA TYPES
# ============================================================

# Definition:
# Set elements must be immutable/hashable values such as
# integers, floats, strings, and tuples.

data = {10, 20.5, "Python", (1, 2)}

print(data)


# ============================================================
# 11. DICTIONARY
# ============================================================

# Definition:
# A dictionary stores data in the form of key-value pairs.
# Each key is associated with a value.
# Dictionary is represented using curly braces {}.

student = {
    "name": "Raju",
    "age": 21,
    "city": "Hyderabad"
}

print(student)


# ============================================================
# 12. ACCESS DICTIONARY VALUE
# ============================================================

# Definition:
# A dictionary value can be accessed using its key.

student = {
    "name": "Raju",
    "age": 21,
    "city": "Hyderabad"
}

print(student["name"])
print(student["age"])
print(student["city"])


# ============================================================
# 13. DICTIONARY IS MUTABLE
# ============================================================

# Definition:
# A dictionary is mutable, so its values can be changed
# after the dictionary is created.

student = {
    "name": "Raju",
    "age": 21
}

print(student)

student["age"] = 22

print(student)


# ============================================================
# 14. ADD NEW KEY-VALUE PAIR
# ============================================================

# Definition:
# We can add a new key-value pair to a dictionary
# by assigning a value to a new key.

student = {
    "name": "Raju",
    "age": 21
}

student["city"] = "Hyderabad"

print(student)


# ============================================================
# 15. DELETE KEY-VALUE PAIR
# ============================================================

# Definition:
# The del keyword can be used to delete a key-value pair.

student = {
    "name": "Raju",
    "age": 21,
    "city": "Hyderabad"
}

del student["city"]

print(student)


# ============================================================
# 16. DICTIONARY KEYS MUST BE UNIQUE
# ============================================================

# Definition:
# Dictionary keys must be unique.
# If the same key is written more than once,
# the latest value replaces the previous value.

student = {
    "name": "Raju",
    "age": 21,
    "age": 25
}

print(student)

# age becomes 25.


# ============================================================
# 17. DICTIONARY VALUES CAN BE DUPLICATED
# ============================================================

# Definition:
# Dictionary values can contain duplicate values.

student = {
    "maths": 90,
    "python": 90,
    "sql": 80
}

print(student)


# ============================================================
# 18. ACCESSING NON-EXISTING KEY
# ============================================================

# Definition:
# Accessing a dictionary using a key that does not exist
# raises a KeyError.

student = {
    "name": "Raju",
    "age": 21
}

# print(student["marks"])
# KeyError: 'marks'


# ============================================================
# 19. DICTIONARY get() METHOD
# ============================================================

# Definition:
# get() safely returns the value associated with a key.
# If the key does not exist, it returns None by default.

student = {
    "name": "Raju",
    "age": 21
}

print(student.get("name"))
print(student.get("marks"))


# ============================================================
# 20. get() WITH DEFAULT VALUE
# ============================================================

# Definition:
# get() can return a specified default value
# when the key does not exist.

student = {
    "name": "Raju",
    "age": 21
}

print(student.get("marks", 0))


# ============================================================
# 21. DICTIONARY KEYS AND VALUES
# ============================================================

# Definition:
# keys() returns all dictionary keys.
# values() returns all dictionary values.
# items() returns key-value pairs.

student = {
    "name": "Raju",
    "age": 21,
    "city": "Hyderabad"
}

print(student.keys())
print(student.values())
print(student.items())


# ============================================================
# 22. SET VS DICTIONARY
# ============================================================

# Definition:
# A set stores unique values.
# A dictionary stores key-value pairs.

my_set = {10, 20, 30}

my_dictionary = {
    "a": 10,
    "b": 20,
    "c": 30
}

print(my_set)
print(my_dictionary)


# ============================================================
# 23. BOOLEAN
# ============================================================

# Definition:
# Boolean is a data type that represents only two values:
# True and False.

is_logged_in = True
is_admin = False

print(is_logged_in)
print(is_admin)

print(type(is_logged_in))


# ============================================================
# 24. COMPARISON OPERATORS RETURN BOOLEAN
# ============================================================

# Definition:
# Comparison operators compare values and return
# either True or False.

print(10 == 10)
print(10 > 5)
print(10 < 20)
print(10 < 5)
print(10 != 20)


# ============================================================
# 25. BOOLEAN WITH VARIABLES
# ============================================================

# Definition:
# A boolean variable stores either True or False.

is_student = True
is_employee = False

print(is_student)
print(is_employee)


# ============================================================
# 26. NONE
# ============================================================

# Definition:
# None represents the absence of a value or no value.
# None is the only value of the NoneType data type.

payment_status = None

print(payment_status)
print(type(payment_status))


# ============================================================
# 27. NONE REAL-TIME EXAMPLE
# ============================================================

# Definition:
# None can be used when a variable does not have
# an actual value yet.

employee_name = None

print(employee_name)

employee_name = "Raju"

print(employee_name)


# ============================================================
# 28. TYPE CASTING
# ============================================================

# Definition:
# Type casting is the process of converting
# one data type into another data type.

# Examples:
# int -> float
# int -> str
# float -> int
# string -> int


# ============================================================
# 29. IMPLICIT TYPE CASTING
# ============================================================

# Definition:
# Implicit type casting is automatic conversion
# performed by Python when appropriate.

a = 10
b = 12.5

result = a + b

print(result)
print(type(result))

# int + float -> float


# ============================================================
# 30. BOOLEAN IN IMPLICIT CONVERSION
# ============================================================

# Definition:
# In numeric operations, True behaves like 1
# and False behaves like 0.

a = True
b = 5

result = a + b

print(result)

# True = 1
# Therefore:
# 1 + 5 = 6


# ============================================================
# 31. EXPLICIT TYPE CASTING
# ============================================================

# Definition:
# Explicit type casting is manual conversion performed
# by the programmer using built-in functions.

a = 10

print(float(a))
print(str(a))
print(bool(a))


# ============================================================
# 32. int() CONVERSION
# ============================================================

# Definition:
# int() converts a compatible value into an integer.

a = "10"

b = int(a)

print(b)
print(type(b))


# ============================================================
# 33. float() CONVERSION
# ============================================================

# Definition:
# float() converts a compatible value into a floating-point number.

a = 10

b = float(a)

print(b)
print(type(b))


# ============================================================
# 34. str() CONVERSION
# ============================================================

# Definition:
# str() converts a value into a string.

a = 100

b = str(a)

print(b)
print(type(b))


# ============================================================
# 35. bool() CONVERSION
# ============================================================

# Definition:
# bool() converts a value into True or False.

a = 10

b = bool(a)

print(b)
print(type(b))


# ============================================================
# 36. FLOAT TO INTEGER
# ============================================================

# Definition:
# int() removes the decimal part when converting
# a float into an integer.
# It does not round the value.

a = 10.75

b = int(a)

print(b)

# Output:
# 10


# ============================================================
# 37. STRING TO INTEGER
# ============================================================

# Definition:
# A numeric string can be converted into an integer
# using int().

x = "10"

y = int(x)

print(y)
print(type(y))


# ============================================================
# 38. STRING TO FLOAT
# ============================================================

# Definition:
# A numeric string can be converted into a float
# using float().

x = "10.5"

y = float(x)

print(y)
print(type(y))


# ============================================================
# 39. STRING TO BOOLEAN
# ============================================================

# Definition:
# A non-empty string converts to True using bool().
# An empty string converts to False.

x = "Python"

print(bool(x))

y = ""

print(bool(y))


# ============================================================
# 40. BOOLEAN TO INTEGER
# ============================================================

# Definition:
# True converts to 1 and False converts to 0
# when converted to integer.

print(int(True))
print(int(False))


# ============================================================
# 41. BOOLEAN TO FLOAT
# ============================================================

# Definition:
# Boolean values can be converted into floating-point numbers.

print(float(True))
print(float(False))


# ============================================================
# 42. BOOLEAN TO STRING
# ============================================================

# Definition:
# str() converts a boolean value into a string.

print(str(True))
print(str(False))


# ============================================================
# 43. LIST TO TUPLE
# ============================================================

# Definition:
# tuple() converts an iterable such as a list into a tuple.

numbers = [10, 20, 30]

result = tuple(numbers)

print(result)
print(type(result))


# ============================================================
# 44. TUPLE TO LIST
# ============================================================

# Definition:
# list() converts an iterable such as a tuple into a list.

numbers = (10, 20, 30)

result = list(numbers)

print(result)
print(type(result))


# ============================================================
# 45. LIST TO SET
# ============================================================

# Definition:
# set() converts an iterable into a set.
# Duplicate values are automatically removed.

numbers = [10, 20, 20, 30]

result = set(numbers)

print(result)
print(type(result))


# ============================================================
# 46. STRING TO LIST
# ============================================================

# Definition:
# list() converts a string into a list of characters.

name = "Python"

result = list(name)

print(result)


# ============================================================
# 47. STRING TO TUPLE
# ============================================================

# Definition:
# tuple() converts a string into a tuple of characters.

name = "Python"

result = tuple(name)

print(result)


# ============================================================
# 48. STRING TO SET
# ============================================================

# Definition:
# set() converts a string into a set of unique characters.

name = "Python"

result = set(name)

print(result)


# ============================================================
# 49. DICTIONARY CONVERSION
# ============================================================

# Definition:
# dict() can create a dictionary from an iterable
# containing key-value pairs.

data = [
    ("name", "Raju"),
    ("age", 23)
]

student = dict(data)

print(student)


# ============================================================
# 50. INVALID DICTIONARY CONVERSION
# ============================================================

# Definition:
# Each element used to create a dictionary must contain
# exactly two values: one key and one value.

# data = [1, 2]
# result = dict(data)

# This produces TypeError.


# ============================================================
# 51. INTEGER CANNOT DIRECTLY BECOME LIST
# ============================================================

# Definition:
# list(), tuple(), and set() generally require
# an iterable object.

# print(list(10))
# TypeError: 'int' object is not iterable


# ============================================================
# 52. CHECKING DATA TYPES
# ============================================================

# Definition:
# type() is used to check the data type of an object.

name = "Krishna"
age = 22
percentage = 95.5
numbers = [10, 20, 30]
values = (10, 20, 30)
unique_values = {10, 20, 30}
student = {"name": "Krishna"}
status = True
value = None

print(type(name))
print(type(age))
print(type(percentage))
print(type(numbers))
print(type(values))
print(type(unique_values))
print(type(student))
print(type(status))
print(type(value))


# ============================================================
# 53. COMPLETE DATA TYPES PRACTICE
# ============================================================

# Definition:
# Python provides different built-in data types
# for storing different kinds of data.

name = "Krishna"                    # str
age = 22                            # int
salary = 25000.50                  # float
complex_number = 4 + 5j            # complex

numbers_list = [10, 20, 30]        # list
numbers_tuple = (10, 20, 30)       # tuple
numbers_range = range(5)            # range

numbers_set = {10, 20, 30}          # set

student = {
    "name": "Krishna",
    "age": 22
}                                   # dict

is_student = True                   # bool
value = None                        # NoneType

print(name)
print(age)
print(salary)
print(complex_number)
print(numbers_list)
print(numbers_tuple)
print(list(numbers_range))
print(numbers_set)
print(student)
print(is_student)
print(value)


# ============================================================
# 54. FINAL PRACTICE PROGRAM
# ============================================================

# Definition:
# This program combines set, dictionary, boolean,
# None, variables, and type casting.

student_name = "Krishna"
age = "22"
skills = {"Python", "SQL", "HTML", "Python"}

student = {
    "name": student_name,
    "age": int(age),
    "skills": skills
}

is_student = True
placement_status = None

print("Student Name:", student["name"])
print("Age:", student["age"])
print("Skills:", student["skills"])
print("Is Student:", is_student)
print("Placement Status:", placement_status)

print(type(student["age"]))
print(type(student["skills"]))
print(type(is_student))
print(type(placement_status))