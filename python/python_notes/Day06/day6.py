
# ============================================================
# TYPE CONVERSION / TYPE CASTING IN PYTHON
# ============================================================

# Definition:
# Type conversion means converting a value from one data type
# to another data type using built-in functions such as:
# int(), float(), str(), bool(), list(), tuple(), set(), dict()


# ============================================================
# 1. CONVERTING FROM INT
# ============================================================

# Given integer
int_a = 2

# int -> float
float_value = float(int_a)
print(float_value)
# Output: 2.0

# int -> string
string_value = str(int_a)
print(string_value)
# Output: 2

# int -> bool
bool_value = bool(int_a)
print(bool_value)
# Output: True

# int -> list
# Error because int is not iterable
# print(list(int_a))

# int -> set
# Error because int is not iterable
# print(set(int_a))

# int -> tuple
# Error because int is not iterable
# print(tuple(int_a))

# int -> dictionary
# Error because int is not iterable
# print(dict(int_a))


# ============================================================
# 2. CONVERTING FROM FLOAT
# ============================================================

# Given float
float_n = 3.1

# float -> int
int_value = int(float_n)
print(int_value)
# Output: 3
# Decimal part is removed

# float -> string
string_value = str(float_n)
print(string_value)
# Output: 3.1

# float -> bool
bool_value = bool(float_n)
print(bool_value)
# Output: True

# float -> list
# Error because float is not iterable
# print(list(float_n))

# float -> tuple
# Error because float is not iterable
# print(tuple(float_n))

# float -> set
# Error because float is not iterable
# print(set(float_n))

# float -> dictionary
# Error because float is not iterable
# print(dict(float_n))


# ============================================================
# 3. CONVERTING FROM STRING
# ============================================================

# Given string
string_c = "power"

# String -> int
numeric_string = "10"
int_value = int(numeric_string)
print(int_value)
# Output: 10

# String -> int with decimal
# Error
# print(int("10.9"))

# String -> int with alphabet
# Error
# print(int("power"))

# String -> float
float_value = float("10.8")
print(float_value)
# Output: 10.8

# String -> float with invalid string
# Error
# print(float("power"))

# String -> bool
bool_value = bool(string_c)
print(bool_value)
# Output: True
# Non-empty string is True

# String -> list
list_value = list(string_c)
print(list_value)
# Output: ['p', 'o', 'w', 'e', 'r']

# String -> tuple
tuple_value = tuple(string_c)
print(tuple_value)
# Output: ('p', 'o', 'w', 'e', 'r')

# String -> set
set_value = set(string_c)
print(set_value)
# Output: {'p', 'o', 'w', 'e', 'r'}
# Order may vary

# String -> dictionary
# Error because dictionary needs key-value pairs
# print(dict(string_c))


# ============================================================
# 4. CONVERTING FROM LIST
# ============================================================

# Given list
list_d = [1, 2, 3, 4]

# List -> int
# Error
# print(int(list_d))

# List -> float
# Error
# print(float(list_d))

# List -> string
string_value = str(list_d)
print(string_value)
# Output: [1, 2, 3, 4]

# List -> bool
bool_value = bool(list_d)
print(bool_value)
# Output: True

# List -> tuple
tuple_value = tuple(list_d)
print(tuple_value)
# Output: (1, 2, 3, 4)

# List -> set
set_value = set(list_d)
print(set_value)
# Output: {1, 2, 3, 4}

# List -> dictionary
# Error because dictionary needs key-value pairs
# print(dict(list_d))


# ============================================================
# 5. CONVERTING FROM TUPLE
# ============================================================

# Given tuple
tuple_f = (1, 2, 3, 4)

# Tuple -> int
# Error
# print(int(tuple_f))

# Tuple -> float
# Error
# print(float(tuple_f))

# Tuple -> string
string_value = str(tuple_f)
print(string_value)
# Output: (1, 2, 3, 4)

# Tuple -> bool
bool_value = bool(tuple_f)
print(bool_value)
# Output: True

# Tuple -> list
list_value = list(tuple_f)
print(list_value)
# Output: [1, 2, 3, 4]

# Tuple -> set
set_value = set(tuple_f)
print(set_value)
# Output: {1, 2, 3, 4}

# Tuple -> dictionary
# Error because dictionary needs key-value pairs
# print(dict(tuple_f))


# ============================================================
# 6. CONVERTING FROM SET
# ============================================================

# Given set
set_e = {3, 4, 5, 6}

# Set -> int
# Error
# print(int(set_e))

# Set -> float
# Error
# print(float(set_e))

# Set -> string
string_value = str(set_e)
print(string_value)
# Output: {3, 4, 5, 6}

# Set -> bool
bool_value = bool(set_e)
print(bool_value)
# Output: True

# Set -> list
list_value = list(set_e)
print(list_value)
# Output order may vary

# Set -> tuple
tuple_value = tuple(set_e)
print(tuple_value)
# Output order may vary

# Set -> dictionary
# Error because dictionary needs key-value pairs
# print(dict(set_e))


# ============================================================
# 7. CONVERTING FROM DICTIONARY
# ============================================================

# Given dictionary
dict_g = {
    1: 1,
    2: 4,
    3: 9
}

# Dictionary -> int
# Error
# print(int(dict_g))

# Dictionary -> float
# Error
# print(float(dict_g))

# Dictionary -> string
string_value = str(dict_g)
print(string_value)
# Output: {1: 1, 2: 4, 3: 9}

# Dictionary -> bool
bool_value = bool(dict_g)
print(bool_value)
# Output: True

# Dictionary -> list
list_value = list(dict_g)
print(list_value)
# Output: [1, 2, 3]
# Only keys are converted

# Dictionary -> tuple
tuple_value = tuple(dict_g)
print(tuple_value)
# Output: (1, 2, 3)
# Only keys are converted

# Dictionary -> set
set_value = set(dict_g)
print(set_value)
# Output: {1, 2, 3}
# Only keys are converted


# ============================================================
# 8. CONVERTING FROM BOOLEAN
# ============================================================

# Given boolean
boolean = False

# bool -> int
int_value = int(boolean)
print(int_value)
# Output: 0

# True -> int
print(int(True))
# Output: 1

# bool -> float
float_value = float(boolean)
print(float_value)
# Output: 0.0

# True -> float
print(float(True))
# Output: 1.0

# bool -> string
string_value = str(boolean)
print(string_value)
# Output: False

# bool -> list
# Error because bool is not iterable
# print(list(boolean))

# bool -> tuple
# Error because bool is not iterable
# print(tuple(boolean))

# bool -> set
# Error because bool is not iterable
# print(set(boolean))

# bool -> dictionary
# Error because bool is not iterable
# print(dict(boolean))


# ============================================================
# 9. LIST TO DICTIONARY
# ============================================================

# Definition:
# A list can be converted into a dictionary when every element
# contains exactly two values: key and value.

d = [
    ("name", "teja"),
    ("batch", "22"),
    ("subject", "python")
]

result = dict(d)

print(result)

# Output:
# {'name': 'teja', 'batch': '22', 'subject': 'python'}


# ============================================================
# 10. OTHER IMPORTANT DICTIONARY CONVERSIONS
# ============================================================

# Tuple of key-value pairs -> dictionary

data = (
    ("name", "Krishna"),
    ("age", 22)
)

student = dict(data)

print(student)
# Output:
# {'name': 'Krishna', 'age': 22}


# List of lists -> dictionary

data = [
    ["name", "Krishna"],
    ["course", "Python"]
]

student = dict(data)

print(student)
# Output:
# {'name': 'Krishna', 'course': 'Python'}


# ============================================================
# 11. EMPTY COLLECTION CONVERSION
# ============================================================

# Empty collections become False when converted to bool

print(bool([]))
# Output: False

print(bool(()))
# Output: False

print(bool(set()))
# Output: False

print(bool({}))
# Output: False

print(bool(""))
# Output: False


# Non-empty collections become True

print(bool([1, 2]))
# Output: True

print(bool((1, 2)))
# Output: True

print(bool({1, 2}))
# Output: True

print(bool({"name": "Krishna"}))
# Output: True

print(bool("Python"))
# Output: True


# ============================================================
# 12. IMPORTANT STRING TO BOOLEAN EXAMPLE
# ============================================================

print(bool("True"))
# Output: True

print(bool("False"))
# Output: True

# Why?
# Because both are non-empty strings.


# ============================================================
# 13. COMPLETE TYPE CONVERSION PRACTICE
# ============================================================

# Integer
a = 10

print("Integer:", a)
print("Integer to float:", float(a))
print("Integer to string:", str(a))
print("Integer to boolean:", bool(a))


# Float
b = 10.5

print("Float:", b)
print("Float to int:", int(b))
print("Float to string:", str(b))
print("Float to boolean:", bool(b))


# String
c = "123"

print("String:", c)
print("String to int:", int(c))
print("String to float:", float(c))
print("String to list:", list(c))
print("String to tuple:", tuple(c))
print("String to set:", set(c))


# List
d = [1, 2, 3]

print("List:", d)
print("List to string:", str(d))
print("List to tuple:", tuple(d))
print("List to set:", set(d))
print("List to boolean:", bool(d))


# Tuple
e = (1, 2, 3)

print("Tuple:", e)
print("Tuple to string:", str(e))
print("Tuple to list:", list(e))
print("Tuple to set:", set(e))
print("Tuple to boolean:", bool(e))


# Set
f = {1, 2, 3}

print("Set:", f)
print("Set to string:", str(f))
print("Set to list:", list(f))
print("Set to tuple:", tuple(f))
print("Set to boolean:", bool(f))


# Dictionary
g = {
    "name": "Krishna",
    "course": "Python"
}

print("Dictionary:", g)
print("Dictionary to string:", str(g))
print("Dictionary to list:", list(g))
print("Dictionary to tuple:", tuple(g))
print("Dictionary to set:", set(g))
print("Dictionary to boolean:", bool(g))


# ============================================================
# 14. TYPE CHECKING AFTER CONVERSION
# ============================================================

number = 10

a = float(number)
b = str(number)
c = bool(number)

print(a, type(a))
# Output: 10.0 <class 'float'>

print(b, type(b))
# Output: 10 <class 'str'>

print(c, type(c))
# Output: True <class 'bool'>


# ============================================================
# 15. FINAL REAL-TIME EXAMPLE
# ============================================================

# User enters age as input.
# input() always returns a string.

age = input("Enter your age: ")

print("Before conversion:", age)
print("Type:", type(age))

# Convert string to integer
age = int(age)

print("After conversion:", age)
print("Type:", type(age))

if age >= 18:
    print("You are eligible")
else:
    print("You are not eligible")


# ============================================================
# FINAL PRACTICE
# ============================================================

# Type Conversion means:
# One data type -> another data type

# Common functions:
# int()
# float()
# str()
# bool()
# list()
# tuple()
# set()
# dict()

# Important:
# int -> float, str, bool
# float -> int, str, bool
# str -> int, float, bool, list, tuple, set
# list -> str, bool, tuple, set
# tuple -> str, bool, list, set
# set -> str, bool, list, tuple
# dict -> str, bool, list, tuple, set
# bool -> int, float, str