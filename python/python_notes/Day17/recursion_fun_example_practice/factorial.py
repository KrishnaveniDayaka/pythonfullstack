#recursion: It is a programming technique where a function calls
#itself to solve a smaller instance of the same problem
#It continues doing this until it reaches a condition 
#where it no longer make a recursive call this is known as base case

def fact(n):
    if n==1 or n==0: #base case
        return 1
    else:
        return n*fact(n-1) #recursive case

result=fact(5)
print(result)
 
 