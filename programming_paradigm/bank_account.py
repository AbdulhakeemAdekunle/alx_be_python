class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0

    def deposit(self, amount):
        self.amount = amount
        return self.amount + self.account_balance

    def withdraw(self, amount):
        self.amount = amount
        return self.account_balance - self.amount

    def display_balance(self):
        print(f"Current Balance: {self.account_balance}")
