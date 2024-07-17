class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0

    def deposit(self, amount):
        self.amount = amount
        return self.amount + self.account_balance

    def withdraw(self, amount):
        self.amount = amount
        if self.amount <= self.account_balance:
            return self.account_balance - self.amount
        else:
            return "Insufficient funds"

    def display_balance(self):
        print(f"Current Balance: {self.account_balance}")
