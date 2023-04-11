# Made by Taryarlinnthit 4/11/2023
class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        print(f"Current balance is ${self.balance}")
        self.balance += amount
        print("Deposit successful!")
        print(f"Now the current balance is:${self.balance}")

    def withdraw(self, amount):
        print(f"Current balance is ${self.balance}")
        if self.balance > amount:
            self.balance -= amount
            print(f"Withdraw successful. Current balance is:${self.balance}")
        else:
            print("Insufficient money!")
            print(f"Only ${self.balance} left!")


def welcome():
    print("Welcome to the bank! What would you like to do?")
    print("1.Register")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    a = int(input("Enter:"))
    return a


def register():
    name = input("Enter name:")
    id_number = int(input("Enter id:"))
    balance = int(input("Enter amount to deposit:$"))
    acc = BankAccount(name, id_number, balance)
    print(f"Account successfully created for user {name}!")
    print()
    return acc


accounts = []
while True:
    check = welcome()
    if check == 1:
        print("Welcome to registering section!")
        account = register()
        accounts.append(account)

    elif check == 2:
        print("Welcome to deposit section!")
        id_num = int(input("Enter your id:"))
        for account in accounts:
            if id_num == account.account_number:
                print(f"Welcome {account.name}")
                money = int(input("Enter amount:$"))
                account.deposit(money)
                print()
                break
            else:
                print("Error acc not found!")

    elif check == 3:
        print("Welcome to withdraw section")
        id_num = int(input("Enter your id:"))
        for account in accounts:
            if id_num == account.account_number:
                print(f"Welcome {account.name}")
                money = int(input("Enter amount to withdraw:$"))
                account.withdraw(money)
                print()
                break
            else:
                print("Error acc not found!")

    elif check == 4:
        print("Thanks for using the bank! See ya!")
        break
    else:
        print("Error! Please try entering again")
