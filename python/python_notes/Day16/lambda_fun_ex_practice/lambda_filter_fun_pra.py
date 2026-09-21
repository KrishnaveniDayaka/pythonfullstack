
#filter() examples
#example1
#syntax:filter(function,iterable)
numbers=[1,5,9,2,4,10,8]
result=list(filter(lambda x:x%2==0,numbers))
res=list(filter(lambda x:x%2!=0,numbers))
print(res)
print(result)

