#what is generator 
#A generator is a special type of function that generates values one at a time 
# using the yield keyword, instead of returning all values at once
#Easy way to remember
#Generator = yield + one value at a time + saves memory
def name():
    print("Start")
    yield 1
    yield 2
g=name()
print(g)
print(next(g))
print(next(g))


