#list :It is a collection of items
#A list comprehension is a short and powerful way to create 
# new lists by using a loop in one line.
#basic syntax :x=[expression for item in iterable if condition ]

items=[2,10,15,33,12,9]
square_of_odditems=[x*x for x in items if x%2!=0]
print(square_of_odditems)

