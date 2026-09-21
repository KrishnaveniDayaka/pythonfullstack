
# Constructor in Python
# __init__() is a special method that is automatically called
# when an object is created.
# It is mainly used to initialize instance variables.
class College:
    def __init__(self,name,branch):
        self.name=name
        self.Branch=branch
        print(self.name," " ,self.Branch)
        
s1=College("LBRCE","CSE")
s2=College("LBRCE","ECE")
