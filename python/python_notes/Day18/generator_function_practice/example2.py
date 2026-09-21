
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
counter = count_up_to(5)
print(next(counter)) # Output: 1
print(next(counter)) # Output: 2