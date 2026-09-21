t = (10, 20, "Krishna", 13.2, "Veni")

print(t)
print(type(t))

# Indexing
print(t[0])
print(t[2])

# Negative indexing
print(t[-1])

# Slicing
print(t[1:4])
print(t[::-1])

# Membership
print(20 in t)
print(100 not in t)

# Built-in functions
print(len(t))
print(min((10, 20, 30)))
print(max((10, 20, 30)))
print(sum((10, 20, 30)))

# Tuple methods
print(t.count(10))
print(t.index("Krishna"))
