
n=int(input("enter n value:"))
end=int(input("Enter end value:"))
for n in range(n,end+1):
    if n<=1:
        continue
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)