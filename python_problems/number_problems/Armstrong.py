
n=int(input("enter a number:"))
temp=n
count=0
while n>0:
    last=n%10
    count+=1
    n=n//10
temp=n
sum=0

while n>0:
    lastdigit=n%10
    sum=sum+lastdigit**count
    n=n//10
if temp==sum:
    print("Armstrong",temp)