
#LEGB rule : Python searched variables in the following order
#local,enclosing,global,built-in

x=100    #global variable
def outer():
    x=50 
    print( "This is enclosing variable:", x)  #enclosing variable
    def inner():
        #x=20 #local variable
        print("This is local variable :", x)
    inner()
outer()