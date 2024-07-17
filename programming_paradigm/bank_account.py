class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance
        
    def deposit(self, amount):
        self.amount = amount
        dp_amount = self.amount + self.account_balance

    def withdraw(self, amount):
        self.amount = amount
        if self.amount <= self.account_balance:
            wd_amount = self.account_balance - self.amount
            return True
        else:
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:2f}")
