
n=int(input("Enter a number:"))
temp=n
rev=0
while n>0:
    lastdigit=n%10
    rev=rev*10+lastdigit
    n=n//10
if rev==temp:
    print("Palindrome ",temp)
else:
    print("Not a palindrome ",temp)