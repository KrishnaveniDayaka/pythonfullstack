
#Nonlocal scope:
#used in nested functions Allows modification of variables from the outer function
def outer():
    count=10
    def inner():
        nonlocal count
        count+=5
    inner()
    print(count)
outer()