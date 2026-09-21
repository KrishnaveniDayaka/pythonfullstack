
#What is lambda?
#Lambda is a function without name A lambda function in Python is a small, anonymous function 
# that can take any number of arguments but contains only one expression.
#  It is created using the lambda keyword
#it is accepts any number of arguments but only one expression

#lambda aruguments:expression
#Example1
square=lambda x:x*x
print(square(5))
print(square(10))
print(square(12))

#Example2

greet=lambda :"Welcome to Lambda functions"
print(greet())

#example 3
add=lambda a,b:a+b
result=add(30,50)
print(f"Addition of two number is  {result}" )

#example 4 
product=lambda c,d:c*d
res=product(40,2)
print(f"Product of two numbers is {res}")





