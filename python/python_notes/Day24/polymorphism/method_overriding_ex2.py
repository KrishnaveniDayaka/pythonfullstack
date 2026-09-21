class Bank:
    def interest(self):
        print("Bank gives normal interest")
class SBI(Bank):
    def interest(self):
        print("SBI gives 7% interest")
class HDFC(Bank):
    def interest(self):
        print("HDFC gives 6% interest")
b = Bank()
s = SBI()
h = HDFC()
b.interest()
s.interest()
h.interest()