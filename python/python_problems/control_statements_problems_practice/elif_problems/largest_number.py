a=int(input("Enter a Value:"))
b=int(input("Enter b Value:"))
c=int(input("Enter c Value:"))
if a>b and a>c:
    print(f"{a} is a largest number")
elif b>c and b>a:
    print(f"{b} is a largest number")
else:
    print(f"{c} is a largest number")



#Output case 1:
Enter a Value:100
Enter b Value: 50
Enter c Value:300
300 is a largest number


#output case 2:
Enter a Value:10
Enter b Value:5
Enter c Value:3
10 is a largest number

#output case 3:
Enter a Value:50
Enter b Value:500
Enter c Value:30
500 is a largest number

    
