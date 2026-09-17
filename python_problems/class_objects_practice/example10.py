
class Bank:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.new_holder=[]
    def account_holder(self,new_holder):
        self.new_holder=[]
        self.new_holder.append(new_holder)
        print("New account holder name is ",self.new_holder)
    def display(self):
        print("Account Name is ",self.name)
        print("Account holder location is ",self.location)
name=input("Enter name")
location=input("Enter location")
new_holder=input("Enter new account holder name is:")
b=Bank(name,location)
b.account_holder("raju")
b.account_holder("venky")
b.account_holder("sai")
b.account_holder("naga")
b.account_holder("saru")
b.display()
