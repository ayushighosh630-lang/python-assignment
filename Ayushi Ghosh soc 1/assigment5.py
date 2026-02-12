class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}, new balance is {self.balance}")
        else:
            print("Invalid amount. Deposit failed.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}, new balance is {self.balance}")
        else:
            print("Invalid amount. Withdrawal failed.")

    def get_balance(self):
        return self.balance


acc = BankAccount("1234567890", 1000)
acc.deposit(500)
acc.withdraw(300)
print("Final Balance:", acc.get_balance())