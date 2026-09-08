import numpy as np
import time

print("=" * 60)
print("        NUMPY COMPLETE PRACTICE PROGRAM")
print("=" * 60)


# ============================================================
# 1. 1D, 2D AND 3D ARRAYS
# ============================================================

print("\n1. 1D, 2D and 3D Arrays")

arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:")
print(arr2)

arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("3D Array:")
print(arr3)


# ============================================================
# 2. ARRAYS WITH SPECIFIC VALUES
# ============================================================

print("\n2. Arrays with Specific Values")

zeros = np.zeros((3, 3))
print("Zeros:")
print(zeros)

ones = np.ones((2, 4))
print("Ones:")
print(ones)

identity = np.eye(4)
print("Identity Matrix:")
print(identity)

full_array = np.full((2, 3), 7)
print("Full Array:")
print(full_array)


# ============================================================
# 3. RANGE OF NUMBERS
# ============================================================

print("\n3. Range of Numbers")

range_arr = np.arange(1, 11, 2)
print("Arange:", range_arr)

lin_space = np.linspace(0, 100, 5)
print("Linspace:", lin_space)


# ============================================================
# 4. RANDOM NUMBER GENERATION
# ============================================================

print("\n4. Random Number Generation")

rand_int = np.random.randint(1, 100, (3, 3))
print("Random Integers:")
print(rand_int)

rand_float = np.random.rand(3, 3)
print("Random Floats:")
print(rand_float)

rand_norm = np.random.randn(3, 3)
print("Random Normal Values:")
print(rand_norm)

rand_choice = np.random.choice(
    [10, 20, 30, 40, 50],
    5
)

print("Random Choice:")
print(rand_choice)

# Seed
np.random.seed(42)

rand_arr = np.random.rand(5)
print("Seeded Random Array:")
print(rand_arr)


# ============================================================
# 5. SHAPE, RESHAPE, FLATTEN AND TRANSPOSE
# ============================================================

print("\n5. Shape, Reshape, Flatten and Transpose")

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Original Array:")
print(arr)

print("Shape:", arr.shape)

reshaped = arr.reshape(3, 2)

print("Reshaped Array:")
print(reshaped)

flattened = arr.flatten()

print("Flattened Array:")
print(flattened)

print("Transpose:")
print(arr.T)


# ============================================================
# 6. INDEXING AND SLICING
# ============================================================

print("\n6. Indexing and Slicing")

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)

print("First Element:", arr[0])
print("Last Element:", arr[-1])

print("Index 1 to 3:", arr[1:4])
print("First 3 Elements:", arr[:3])
print("Every 2nd Element:", arr[::2])


# ---------------- 2D Indexing ----------------

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n2D Matrix:")
print(matrix)

print("Element at [1,2]:", matrix[1, 2])

print("Column 1:")
print(matrix[:, 1])

print("Rows 0-1 and Columns 1-2:")
print(matrix[0:2, 1:3])


# ============================================================
# 7. MATHEMATICAL OPERATIONS
# ============================================================

print("\n7. Mathematical Operations")

arr = np.array([1, 2, 3, 4, 5])

print("Original:", arr)

print("Add 10:", arr + 10)
print("Multiply by 2:", arr * 2)
print("Square:", arr ** 2)
print("Square Root:", np.sqrt(arr))


# ============================================================
# 8. AGGREGATE FUNCTIONS
# ============================================================

print("\n8. Aggregate Functions")

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))

print("Cumulative Sum:", np.cumsum(arr))
print("Cumulative Product:", np.cumprod(arr))


# ============================================================
# 9. BOOLEAN INDEXING
# ============================================================

print("\n9. Boolean Indexing")

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)

print("Values greater than 25:")
print(arr[arr > 25])

print("Values less than 40:")
print(arr[arr < 40])

print("Values greater than or equal to 30:")
print(arr[arr >= 30])


# ============================================================
# 10. LINEAR ALGEBRA
# ============================================================

print("\n10. Linear Algebra")

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

# Matrix multiplication
print("Dot Product:")
print(np.dot(A, B))

# Determinant
print("Determinant of A:")
print(np.linalg.det(A))

# Inverse
print("Inverse of A:")
print(np.linalg.inv(A))

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)

# Solving equations
C = np.array([5, 11])

print("Solution of AX = C:")
print(np.linalg.solve(A, C))


# ============================================================
# 11. SORTING AND UNIQUE
# ============================================================

print("\n11. Sorting and Unique")

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

print("Original:", arr)

print("Sorted:", np.sort(arr))

print("Unique Values:", np.unique(arr))


# ============================================================
# 12. STACKING AND SPLITTING
# ============================================================

print("\n12. Stacking and Splitting")

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# Vertical stacking
vertical = np.vstack((A, B))

print("Vertical Stack:")
print(vertical)

# Horizontal stacking
horizontal = np.hstack((A, B))

print("Horizontal Stack:")
print(horizontal)

# Splitting
split_arr = np.split(
    np.array([1, 2, 3, 4, 5, 6]),
    3
)

print("Split Array:")
print(split_arr)


# ============================================================
# 13. COPY VS VIEW
# ============================================================

print("\n13. Copy vs View")

arr = np.array([10, 20, 30])

print("Original Array:", arr)

# View
view_arr = arr.view()

view_arr[0] = 100

print("After changing View:")
print("Original:", arr)
print("View:", view_arr)

# Copy
copy_arr = arr.copy()

copy_arr[0] = 200

print("\nAfter changing Copy:")
print("Original:", arr)
print("Copy:", copy_arr)


# ============================================================
# 14. PYTHON LIST VS NUMPY ARRAY
# ============================================================

print("\n14. Python List vs NumPy Array")

# Python List
lst = [1, "apple", 3.5]

print("Python List:")
print(lst)

# NumPy Array
arr = np.array([1, 2, 3])

print("NumPy Array:")
print(arr)


# ============================================================
# 15. ELEMENT-WISE OPERATIONS
# ============================================================

print("\n15. Element-wise Operations")

# List
lst = [1, 2, 3]

doubled_list = [x * 2 for x in lst]

print("List Doubled:")
print(doubled_list)

# NumPy
arr = np.array([1, 2, 3])

doubled_array = arr * 2

print("NumPy Array Doubled:")
print(doubled_array)


# ============================================================
# 16. SPEED COMPARISON
# ============================================================

print("\n16. Speed Comparison")

lst1 = list(range(1_000_000))
lst2 = list(range(1_000_000))

# List operation
start = time.time()

result_list = [
    x + y
    for x, y in zip(lst1, lst2)
]

list_time = time.time() - start

print("List Time:", list_time)


# NumPy operation
arr1 = np.array(lst1)
arr2 = np.array(lst2)

start = time.time()

result_array = arr1 + arr2

array_time = time.time() - start

print("NumPy Array Time:", array_time)


# ============================================================
# 17. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("                  FINAL SUMMARY")
print("=" * 60)

print("""
1. np.array()       -> Create arrays
2. np.zeros()       -> Create array with zeros
3. np.ones()        -> Create array with ones
4. np.eye()         -> Create identity matrix
5. np.full()        -> Fill array with one value
6. np.arange()      -> Create range of numbers
7. np.linspace()    -> Create equally spaced numbers
8. np.random        -> Generate random numbers
9. shape            -> Find dimensions
10. reshape()       -> Change array shape
11. flatten()       -> Convert to 1D
12. T               -> Transpose array
13. Indexing         -> Access elements
14. Slicing          -> Access a range of elements
15. Mathematical     -> Perform calculations
16. Aggregate        -> sum, mean, median, etc.
17. Boolean Indexing  -> Filter data
18. Linear Algebra   -> Matrix calculations
19. Sorting          -> Sort values
20. Unique           -> Remove duplicate values
21. vstack()         -> Vertical stacking
22. hstack()         -> Horizontal stacking
23. split()          -> Split arrays
24. view()           -> Shared memory
25. copy()           -> Separate memory
26. NumPy            -> Faster numerical operations
""")

print("=" * 60)
print("              PROGRAM COMPLETED")
print("=" * 60)