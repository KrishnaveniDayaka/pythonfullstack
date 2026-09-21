
n=int(input("enter n"))
count=0
sum=0
while n>0:
    lastdigit=n%10
    sum=sum+lastdigit
    count+=1
    n=n//10
print(count)
print(sum)