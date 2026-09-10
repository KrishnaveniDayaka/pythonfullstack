
n=int(input("Enter a number:"))
num=n+1
i=1
while i*i<=num:
    if i*i==num:
        print(i*i)
        print(n," is a sunny number")
        break
    i=i+1
else:
    print(n," is not a sunny number")