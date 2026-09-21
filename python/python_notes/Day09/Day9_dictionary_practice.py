# ==========================================
# DAY 9 - DICTIONARY PRACTICE
# ==========================================


# ------------------------------------------
# 1. Creating a Dictionary
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22,
    "course": "Python Full Stack"
}

print(student)
print(type(student))


# ------------------------------------------
# 2. Empty Dictionary
# ------------------------------------------

d = {}

print(d)
print(type(d))


# ------------------------------------------
# 3. Dictionary with Different Data Types
# ------------------------------------------

data = {
    "name": "Krishna",
    "age": 22,
    "marks": 85.5,
    "passed": True
}

print(data)


# ------------------------------------------
# 4. Key-Value Pairs
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22,
    "city": "Hyderabad"
}

print(student["name"])
print(student["age"])
print(student["city"])


# ------------------------------------------
# 5. Accessing Values using get()
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22
}

print(student.get("name"))
print(student.get("age"))

# If key does not exist
print(student.get("course"))

# Returns None


# ------------------------------------------
# 6. get() with Default Value
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22
}

print(student.get("course", "Not Available"))


# ------------------------------------------
# 7. Adding New Key-Value Pair
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22
}

student["course"] = "Python Full Stack"

print(student)


# ------------------------------------------
# 8. Updating Existing Value
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22
}

student["age"] = 23

print(student)


# ------------------------------------------
# 9. Updating Multiple Values
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22
}

student.update({
    "age": 23,
    "city": "Hyderabad",
    "course": "Python"
})

print(student)


# ------------------------------------------
# 10. Duplicate Keys
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22,
    "age": 23
}

print(student)

# Last value is stored.


# ------------------------------------------
# 11. Dictionary Keys Must Be Unique
# ------------------------------------------

d = {
    1: "One",
    2: "Two",
    3: "Three"
}

print(d)


# ------------------------------------------
# 12. len()
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22,
    "city": "Hyderabad"
}

print(len(student))


# ------------------------------------------
# 13. Membership Operator
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22,
    "city": "Hyderabad"
}

print("name" in student)
print("age" in student)
print("course" in student)

print("name" not in student)


# ------------------------------------------
# 14. keys()
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22,
    "city": "Hyderabad"
}

print(student.keys())


# ------------------------------------------
# 15. values()
# ------------------------------------------

print(student.values())


# ------------------------------------------
# 16. items()
# ------------------------------------------

print(student.items())


# ------------------------------------------
# 17. Loop Through Dictionary
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22,
    "city": "Hyderabad"
}

for key in student:
    print(key)


# ------------------------------------------
# 18. Loop Through Keys
# ------------------------------------------

for key in student.keys():
    print(key)


# ------------------------------------------
# 19. Loop Through Values
# ------------------------------------------

for value in student.values():
    print(value)


# ------------------------------------------
# 20. Loop Through Keys and Values
# ------------------------------------------

for key, value in student.items():
    print(key, ":", value)


# ------------------------------------------
# 21. pop()
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22,
    "city": "Hyderabad"
}

result = student.pop("age")

print("Removed:", result)
print(student)


# ------------------------------------------
# 22. pop() with Default Value
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22
}

result = student.pop("salary", "Not Found")

print(result)


# ------------------------------------------
# 23. popitem()
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22,
    "city": "Hyderabad"
}

result = student.popitem()

print("Removed:", result)
print(student)


# ------------------------------------------
# 24. clear()
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22
}

student.clear()

print(student)


# ------------------------------------------
# 25. copy()
# ------------------------------------------

student1 = {
    "name": "Krishna",
    "age": 22
}

student2 = student1.copy()

print(student1)
print(student2)


# ------------------------------------------
# 26. setdefault()
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22
}

student.setdefault("city", "Hyderabad")

print(student)


# If key already exists,
# value will not be changed.

student.setdefault("age", 30)

print(student)


# ------------------------------------------
# 27. Dictionary using dict()
# ------------------------------------------

student = dict(
    name="Krishna",
    age=22,
    course="Python"
)

print(student)


# ------------------------------------------
# 28. Dictionary from List of Tuples
# ------------------------------------------

data = [
    ("name", "Krishna"),
    ("age", 22),
    ("city", "Hyderabad")
]

student = dict(data)

print(student)


# ------------------------------------------
# 29. Dictionary with Integer Keys
# ------------------------------------------

numbers = {
    1: "One",
    2: "Two",
    3: "Three"
}

print(numbers[1])
print(numbers[2])


# ------------------------------------------
# 30. Dictionary with Tuple Keys
# ------------------------------------------

data = {
    (10, 20): "Point A",
    (30, 40): "Point B"
}

print(data[(10, 20)])


# ------------------------------------------
# 31. Dictionary with List Values
# ------------------------------------------

student = {
    "name": "Krishna",
    "marks": [80, 85, 90]
}

print(student)
print(student["marks"])

print(student["marks"][0])
print(student["marks"][1])


# ------------------------------------------
# 32. Dictionary with Tuple Values
# ------------------------------------------

student = {
    "name": "Krishna",
    "marks": (80, 85, 90)
}

print(student)
print(student["marks"])


# ------------------------------------------
# 33. Dictionary with Set Values
# ------------------------------------------

data = {
    "numbers": {10, 20, 30}
}

print(data)


# ------------------------------------------
# 34. Nested Dictionary
# ------------------------------------------

students = {
    "student1": {
        "name": "Krishna",
        "age": 22
    },

    "student2": {
        "name": "Veni",
        "age": 23
    }
}

print(students)


# Access nested dictionary

print(students["student1"])

print(students["student1"]["name"])
print(students["student1"]["age"])


# ------------------------------------------
# 35. Dictionary with Multiple Students
# ------------------------------------------

students = {
    101: {
        "name": "Krishna",
        "marks": 85
    },

    102: {
        "name": "Veni",
        "marks": 90
    },

    103: {
        "name": "Ravi",
        "marks": 78
    }
}

print(students)

print(students[101]["name"])
print(students[102]["marks"])


# ------------------------------------------
# 36. Loop Through Nested Dictionary
# ------------------------------------------

for student_id, details in students.items():

    print("Student ID:", student_id)

    for key, value in details.items():
        print(key, ":", value)


# ------------------------------------------
# 37. Check Key Exists
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22
}

if "name" in student:
    print("Name exists")


if "salary" not in student:
    print("Salary does not exist")


# ------------------------------------------
# 38. Dictionary Length
# ------------------------------------------

student = {
    "name": "Krishna",
    "age": 22,
    "city": "Hyderabad",
    "course": "Python"
}

print("Number of keys:", len(student))


# ------------------------------------------
# 39. Find Maximum Value
# ------------------------------------------

marks = {
    "Krishna": 85,
    "Veni": 92,
    "Ravi": 78
}

print(max(marks.values()))


# ------------------------------------------
# 40. Find Minimum Value
# ------------------------------------------

print(min(marks.values()))


# ------------------------------------------
# 41. Sum of Values
# ------------------------------------------

print(sum(marks.values()))


# ------------------------------------------
# 42. Character Frequency
# ------------------------------------------

text = "python"

frequency = {}

for char in text:

    if char in frequency:
        frequency[char] += 1

    else:
        frequency[char] = 1

print(frequency)


# ------------------------------------------
# 43. Word Frequency
# ------------------------------------------

text = "python java python c java python"

words = text.split()

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] += 1

    else:
        frequency[word] = 1

print(frequency)


# ------------------------------------------
# 44. Student Marks
# ------------------------------------------

student = {
    "name": "Krishna",
    "maths": 85,
    "science": 90,
    "english": 80
}

total = (
    student["maths"]
    + student["science"]
    + student["english"]
)

print("Total:", total)


# ------------------------------------------
# 45. Student Average
# ------------------------------------------

average = total / 3

print("Average:", average)


# ------------------------------------------
# 46. Student Result
# ------------------------------------------

if average >= 40:
    print("Pass")
else:
    print("Fail")


# ------------------------------------------
# 47. Dictionary Comprehension
# ------------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = {
    num: num ** 2
    for num in numbers
}

print(squares)


# ------------------------------------------
# 48. Dictionary Comprehension with Condition
# ------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = {
    num: num ** 2
    for num in numbers
    if num % 2 == 0
}

print(even_numbers)


# ------------------------------------------
# 49. Convert Two Lists into Dictionary
# ------------------------------------------

keys = ["name", "age", "city"]

values = ["Krishna", 22, "Hyderabad"]

student = dict(zip(keys, values))

print(student)


# ------------------------------------------
# 50. Practical Example
# Employee Details
# ------------------------------------------

employee = {
    "id": 101,
    "name": "Krishna",
    "salary": 50000,
    "department": "IT"
}

print("Employee ID:", employee["id"])
print("Name:", employee["name"])
print("Salary:", employee["salary"])
print("Department:", employee["department"])


# ------------------------------------------
# 51. Practical Example
# Product Details
# ------------------------------------------

product = {
    "id": 101,
    "name": "Laptop",
    "price": 55000,
    "brand": "HP"
}

print(product)


# Update price

product["price"] = 60000

print(product)


# ------------------------------------------
# 52. Practical Example
# Shopping Cart
# ------------------------------------------

cart = {
    "Laptop": 55000,
    "Mouse": 1000,
    "Keyboard": 2000
}

total = sum(cart.values())

print("Cart Total:", total)


# ------------------------------------------
# 53. Practical Example
# Find Highest Marks Student
# ------------------------------------------

marks = {
    "Krishna": 85,
    "Veni": 95,
    "Ravi": 78,
    "Anu": 88
}

highest_student = max(
    marks,
    key=marks.get
)

print("Highest Marks:", highest_student)
print("Marks:", marks[highest_student])


# ------------------------------------------
# 54. Practical Example
# Find Lowest Marks Student
# ------------------------------------------

lowest_student = min(
    marks,
    key=marks.get
)

print("Lowest Marks:", lowest_student)
print("Marks:", marks[lowest_student])


# ------------------------------------------
# 55. Practical Example
# Merge Dictionaries
# ------------------------------------------

dict1 = {
    "name": "Krishna",
    "age": 22
}

dict2 = {
    "city": "Hyderabad",
    "course": "Python"
}

dict1.update(dict2)

print(dict1)


# ------------------------------------------
# 56. Practical Example
# Remove Duplicate Values
# ------------------------------------------

data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30
}

unique_values = set(data.values())

print(unique_values)


# ------------------------------------------
# 57. Important Difference
# ------------------------------------------

# List
list1 = [10, 20, 30]

# Tuple
tuple1 = (10, 20, 30)

# Set
set1 = {10, 20, 30}

# Dictionary
dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

print(list1)
print(tuple1)
print(set1)
print(dict1)


# ==========================================
# END OF DAY 9 - DICTIONARY PRACTICE
# ==========================================
