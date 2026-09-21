
#pass by value:
#when immutable objects are passed to a function changes 
#inside the function do not affect the original value
#immutable types:int,float,complex,str,tuple,bool,frozenset

def update(number):
    number=77
    print("Inside Function:",number)
value=50
update(value)
print("Outside function:",value)
#original vaule remains unchanged
