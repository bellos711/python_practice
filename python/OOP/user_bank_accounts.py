
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


class User:
    def __init__(self, name, email, account_count=0):
        self.name = name
        self.email = email
        self.account_count = account_count
        if self.account_count == 0:
            self.account = BankAccount(int_rate=0.02, balance=0)
        else:
            self.account=[]
            for i in range(0, self.account_count, 1):
                self.account.append(BankAccount(int_rate=0.02, balance=0)) #= BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount, account_index=0):
        #self.account_balance += amount
        if self.account_count == 0:
            self.account.deposit(amount)
            return self
        else:
            self.account[account_index].deposit(amount)
            return self

    def make_withdraw(self, amount, account_index=0):
        #self.account_balance -= amount
        if self.account_count == 0:
            self.account.withdraw(amount)
            return self
        else:
            self.account[account_index].withdraw(amount)
            return self

    def display_user_balance(self, account_index=0):
        if self.account_count==0:
            print(f"User: {self.name}, Balance: {self.account.account_balance}")
        else:
            print(f"User: {self.name}, User Account Number: {account_index}, Balance: {self.account[account_index].account_balance}")

    # EXTRA METHOD
    # def transfer_money(self, other_user, amount):
    #     self.make_withdraw(amount)
    #     other_user.make_deposit(amount)
    #     print(f"you transferred {amount} to {other_user.name}.")
    #     return self

kahlil = User('Kahlil', 'kb@sample.com')
print("USER WITH BANK ACCOUNTS version:")
kahlil.make_deposit(1000).make_deposit(2500).make_deposit(200).make_withdraw(1900).display_user_balance()

print("\n###########################################################")
print("USER WITH MULTIPLE BANK ACCOUNTS ACCESSED THROUGH ARRAY OF OBJECTS")
holmes = User('Holmes', 'hd@sample.com', 2)
print("USER WITH BANK ACCOUNTS version:")
holmes.make_deposit(1000, 1)
holmes.make_withdraw(200, 1)
holmes.display_user_balance(1)

print(f"SAME USER {holmes.name} WITH DIFF ACCOUNT")
holmes.make_deposit(2000, 0)
holmes.make_withdraw(500, 0)
holmes.display_user_balance(0)
