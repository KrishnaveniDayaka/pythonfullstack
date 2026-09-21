import time

# storing accounts using a dictionary
# account number -> details
accounts = {
    "1001": {"name": "Ravi Kumar", "pin": "1234", "balance": 5000.0, "history": []},
    "1002": {"name": "Anjali Sharma", "pin": "5678", "balance": 12000.0, "history": []}
}

locked = set()  # accounts that got locked after wrong pin

max_attempts = 3
min_withdraw = 100


def login():
    acc = input("Enter account number: ")

    if acc not in accounts:
        print("No such account exists")
        return None

    if acc in locked:
        print("Account is locked, too many wrong attempts")
        return None

    tries = 0
    while tries < max_attempts:
        pin = input("Enter pin: ")

        if pin == accounts[acc]["pin"]:
            print("\nWelcome " + accounts[acc]["name"])
            return acc

        tries = tries + 1
        left = max_attempts - tries
        if left > 0:
            print("Wrong pin, attempts left:", left)
        else:
            locked.add(acc)
            print("Too many wrong tries. Account locked now.")

    return None


def show_balance(acc):
    print("Balance:", accounts[acc]["balance"])


def deposit(acc):
    amt = float(input("Enter amount to deposit: "))

    if amt <= 0:
        print("enter a valid amount")
        return

    accounts[acc]["balance"] += amt
    accounts[acc]["history"].append(("deposit", amt, time.ctime()))
    print("Done. New balance:", accounts[acc]["balance"])


def withdraw(acc):
    amt = float(input("Enter amount to withdraw: "))

    if amt <= 0:
        print("enter a valid amount")
        return

    if amt % min_withdraw != 0:
        print("amount should be in multiples of 100")
        return

    if amt > accounts[acc]["balance"]:
        print("not enough balance")
        return

    accounts[acc]["balance"] -= amt
    accounts[acc]["history"].append(("withdraw", amt, time.ctime()))
    print("Done. New balance:", accounts[acc]["balance"])


def change_pin(acc):
    old = input("current pin: ")
    if old != accounts[acc]["pin"]:
        print("wrong pin")
        return

    new = input("new pin (4 digits): ")
    if len(new) == 4 and new.isdigit():
        accounts[acc]["pin"] = new
        print("pin changed")
    else:
        print("pin should be 4 digits")


def history(acc):
    h = accounts[acc]["history"]
    if len(h) == 0:
        print("no transactions yet")
        return

    for t in h:
        print(t[2], "-", t[0], "-", t[1])


def menu(acc):
    while True:
        print("\n1.Balance  2.Deposit  3.Withdraw  4.Change pin  5.History  6.Logout")
        ch = input("choice: ")

        if ch == "1":
            show_balance(acc)
        elif ch == "2":
            deposit(acc)
        elif ch == "3":
            withdraw(acc)
        elif ch == "4":
            change_pin(acc)
        elif ch == "5":
            history(acc)
        elif ch == "6":
            print("logging out...")
            break
        else:
            print("invalid choice")


print("---- ATM ----")
while True:
    acc = login()
    if acc != None:
        menu(acc)

    again = input("another user? (y/n): ")
    if again != "y":
        break

print("thank you")
