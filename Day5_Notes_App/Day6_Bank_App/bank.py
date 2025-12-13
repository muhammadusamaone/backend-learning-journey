class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def show_balance(self):
        print(f"{self.name}'s Balance:", self.balance)


account = BankAccount(input("Enter your name: "))

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    ch = input("Choose: ")

    if ch == "1":
        amt = float(input("Enter amount: "))
        account.deposit(amt)

    elif ch == "2":
        amt = float(input("Enter amount: "))
        account.withdraw(amt)

    elif ch == "3":
        account.show_balance()

    elif ch == "4":
        break

    else:
        print("Invalid option")

