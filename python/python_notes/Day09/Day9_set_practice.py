# ==========================================
# DAY 8 - SET PRACTICE
# ==========================================


# ------------------------------------------
# 1. Creating a Set
# ------------------------------------------

s = {10, 20, 30, 40}

print(s)
print(type(s))


# ------------------------------------------
# 2. Set with Duplicate Values
# ------------------------------------------

s = {10, 20, 30, 10, 20, 30}

print(s)
# Duplicates are automatically removed


# ------------------------------------------
# 3. Empty Set
# ------------------------------------------

s1 = {}

print(type(s1))       # dict

s2 = set()

print(type(s2))       # set


# ------------------------------------------
# 4. Set with Different Data Types
# ------------------------------------------

s = {10, 20.5, "Python", True}

print(s)


# ------------------------------------------
# 5. Set Does Not Support Indexing
# ------------------------------------------

s = {10, 20, 30, 40}

# print(s[0])
# TypeError: 'set' object is not subscriptable


# ------------------------------------------
# 6. Set Does Not Support Slicing
# ------------------------------------------

# print(s[1:3])
# TypeError


# ------------------------------------------
# 7. Membership Operators
# ------------------------------------------

s = {10, 20, 30, 40}

print(20 in s)
print(50 in s)

print(20 not in s)
print(50 not in s)


# ------------------------------------------
# 8. len()
# ------------------------------------------

s = {10, 20, 30, 40}

print(len(s))


# ------------------------------------------
# 9. Adding Elements - add()
# ------------------------------------------

s = {10, 20, 30}

s.add(40)

print(s)

s.add(50)

print(s)


# ------------------------------------------
# 10. Adding Duplicate Element
# ------------------------------------------

s = {10, 20, 30}

s.add(20)

print(s)
# 20 will not be added again


# ------------------------------------------
# 11. Adding Multiple Elements - update()
# ------------------------------------------

s = {10, 20, 30}

s.update([40, 50, 60])

print(s)


# update() with another set

s.update({70, 80})

print(s)


# update() with tuple

s.update((90, 100))

print(s)


# ------------------------------------------
# 12. remove()
# ------------------------------------------

s = {10, 20, 30, 40}

s.remove(20)

print(s)


# If element does not exist,
# remove() gives KeyError

# s.remove(100)


# ------------------------------------------
# 13. discard()
# ------------------------------------------

s = {10, 20, 30, 40}

s.discard(20)

print(s)


# If element does not exist,
# discard() does NOT give error

s.discard(100)

print(s)


# ------------------------------------------
# 14. remove() vs discard()
# ------------------------------------------

s = {10, 20, 30}

# s.remove(100)       # KeyError

s.discard(100)        # No error


# ------------------------------------------
# 15. pop()
# ------------------------------------------

s = {10, 20, 30, 40}

x = s.pop()

print("Removed:", x)
print(s)

# Important:
# Set is unordered, so we cannot predict
# which element pop() will remove.


# ------------------------------------------
# 16. clear()
# ------------------------------------------

s = {10, 20, 30}

s.clear()

print(s)


# ------------------------------------------
# 17. copy()
# ------------------------------------------

s1 = {10, 20, 30}

s2 = s1.copy()

print(s1)
print(s2)


# ------------------------------------------
# 18. Union
# ------------------------------------------

a = {10, 20, 30}
b = {30, 40, 50}

print(a | b)


# Using union() method

print(a.union(b))


# ------------------------------------------
# 19. Intersection
# ------------------------------------------

a = {10, 20, 30}
b = {30, 40, 50}

print(a & b)


# Using intersection()

print(a.intersection(b))


# ------------------------------------------
# 20. Difference
# ------------------------------------------

a = {10, 20, 30}
b = {30, 40, 50}

print(a - b)

print(b - a)


# Using difference()

print(a.difference(b))


# ------------------------------------------
# 21. Symmetric Difference
# ------------------------------------------

a = {10, 20, 30}
b = {30, 40, 50}

print(a ^ b)


# Using symmetric_difference()

print(a.symmetric_difference(b))


# ------------------------------------------
# 22. issubset()
# ------------------------------------------

a = {10, 20}
b = {10, 20, 30, 40}

print(a.issubset(b))


# ------------------------------------------
# 23. issuperset()
# ------------------------------------------

a = {10, 20, 30, 40}
b = {10, 20}

print(a.issuperset(b))


# ------------------------------------------
# 24. isdisjoint()
# ------------------------------------------

a = {10, 20, 30}
b = {40, 50, 60}

print(a.isdisjoint(b))


# ------------------------------------------
# 25. frozenset
# ------------------------------------------

s = frozenset([10, 20, 30])

print(s)
print(type(s))

# frozenset is immutable

# s.add(40)
# AttributeError


# ------------------------------------------
# 26. Set with String
# ------------------------------------------

s = {"Python", "Java", "C", "Python"}

print(s)


# ------------------------------------------
# 27. Set from List
# ------------------------------------------

numbers = [10, 20, 30, 10, 20, 40]

s = set(numbers)

print(s)


# Useful for removing duplicates from a list.


# ------------------------------------------
# 28. Set from String
# ------------------------------------------

name = "python"

s = set(name)

print(s)

# Each unique character becomes an element.


# ------------------------------------------
# 29. Loop Through Set
# ------------------------------------------

s = {10, 20, 30, 40}

for value in s:
    print(value)


# ------------------------------------------
# 30. Set with if condition
# ------------------------------------------

s = {10, 20, 30, 40}

if 20 in s:
    print("20 is present")


# ------------------------------------------
# 31. Find Common Elements
# ------------------------------------------

students_python = {"Krishna", "Veni", "Ravi", "Anu"}

students_java = {"Ravi", "Anu", "Kiran"}

common = students_python & students_java

print("Common students:", common)


# ------------------------------------------
# 32. Find Unique Students
# ------------------------------------------

students_python = {"Krishna", "Veni", "Ravi"}

students_java = {"Ravi", "Anu", "Kiran"}

unique = students_python ^ students_java

print("Unique students:", unique)


# ------------------------------------------
# 33. Remove Duplicates from List
# ------------------------------------------

numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = set(numbers)

print(unique_numbers)


# ------------------------------------------
# 34. Convert Set Back to List
# ------------------------------------------

s = {10, 20, 30, 40}

numbers = list(s)

print(numbers)
print(type(numbers))


# ------------------------------------------
# 35. Nested Set
# ------------------------------------------

# A normal set cannot contain a list
# because list is mutable.

# s = {[10, 20], [30, 40]}
# TypeError


# But frozenset can be an element

s = {frozenset([10, 20]), frozenset([30, 40])}

print(s)


# ------------------------------------------
# 36. Set Comparison
# ------------------------------------------

a = {10, 20, 30}
b = {10, 20, 30}

print(a == b)


# ------------------------------------------
# 37. Practical Example
# Find duplicate values
# ------------------------------------------

numbers = [10, 20, 30, 10, 40, 20, 50]

unique = set()
duplicates = set()

for num in numbers:

    if num in unique:
        duplicates.add(num)

    else:
        unique.add(num)

print("Unique:", unique)
print("Duplicates:", duplicates)


# ------------------------------------------
# 38. Practical Example
# Remove duplicates
# ------------------------------------------

numbers = [1, 2, 2, 3, 4, 4, 5, 5]

numbers = list(set(numbers))

print(numbers)


# ==========================================
# END OF DAY 8 - SET PRACTICE
# ==========================================
