
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def show_balance(self):
        print(f"{self.name},your balance is {self.__balance}")
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"{amount} deposited successfully")
        else:
            print("Invalid deposit amount")
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            print(f"{amount} withdrawn successfully")
        else:
            print("Insufficent balance")
account=BankAccount("Krishna",50000)
account.show_balance()
account.deposit(1000)
account.show_balance()
account.withdraw(100)
account.show_balance()
