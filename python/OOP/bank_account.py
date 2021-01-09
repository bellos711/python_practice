
class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.account_balance = balance
        self.interest_rate = int_rate

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"Your Balance is: ${self.account_balance}")

    def yield_interest(self):
        while self.account_balance>0:
            self.account_balance += self.account_balance*self.interest_rate
            return self
        return self


kahlil = BankAccount(0.03, 500)
kahlil.deposit(500).deposit(600).deposit(400).withdraw(1000).yield_interest().display_user_balance()
print("\n")
holmes = BankAccount(0.05, 300)
holmes.deposit(1000).deposit(700).withdraw(500).withdraw(500).withdraw(500).withdraw(400).yield_interest().display_user_balance()