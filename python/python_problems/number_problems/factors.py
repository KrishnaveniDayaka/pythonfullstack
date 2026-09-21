count=0
sum=0
n=int(input("Enter a number:"))
for i in range(1,n+1):
    if n%i==0:
        print(i)
        count+=1
        sum=sum+i
print("Count of factors:",count)
print(sum)