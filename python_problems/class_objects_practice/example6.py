
class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
            self.balance=self.balance+amount
            print(f"Account Holder name is {self.name} Balance is {self.balance}")
    def withdraw(self,withdraw_amount):
         self.balance=self.balance-withdraw_amount
         print(f"Account Holder name is {self.name} Balance is {self.balance}")
name=input("Enter name ")
balance=int(input("Enter balance:"))
amount=int(input("enter deposit amount:"))
withdraw_amount=int(input("Enter withdrawamount:"))
b=Bank(name,balance)
b.deposit(amount)
b.withdraw(withdraw_amount)