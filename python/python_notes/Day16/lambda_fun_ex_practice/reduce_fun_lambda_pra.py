
#reduce function example
#first from functools import reduce
#syntax reduce(function,iterable)

from functools import reduce
num=[10,20,41,32]
result=reduce(lambda a,b:a*b,num)
print(result)
