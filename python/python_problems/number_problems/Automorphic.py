
n=int(input("Enter a number: "))
square=n*n
temp=n
#count=len(str(temp))
count=0
while temp>0:
    count+=1
    temp=temp//10
last_digit=square%(10**count)
if last_digit==n:
    print(square)
    print(n,"is a automorphic number")
else:
    print(n," is not a automorphic number")
