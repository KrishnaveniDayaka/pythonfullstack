
#pass by refernce :when mutable objects are passed
#to a function ,changes inside the function affect the original object
#mutable types :list,set,dict
def update(items):
    items.append('Laptop')
cart=["mobiles","watch"]
update(cart)
print(cart)
