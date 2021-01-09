
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance=0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdraw(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

    #EXTRA METHOD
    def transfer_money(self, other_user, amount):
        self.make_withdraw(amount)
        other_user.make_deposit(amount)
        print(f"you transferred {amount} to {other_user.name}.")
        return self
        


kahlil = User('Kahlil', 'kb@sample.com')
holmes = User('Holmes', 'hd@sample.com')
stig = User('Stig', 'sg@sample.com')

#Have the first user make 3 deposits and 1 withdrawal and then display their balance
# kahlil.make_deposit(500)
# kahlil.make_deposit(300)
# kahlil.make_deposit(700)
# kahlil.make_withdraw(800)
# kahlil.display_user_balance()
print("Updated version:")
kahlil.make_deposit(500).make_deposit(300).make_deposit(700).make_withdraw(800).display_user_balance()

print("\n")
#user 2 deposits and 2 withdraws
print("Updated version:")
holmes.make_deposit(1000).make_deposit(200).make_withdraw(100).make_withdraw(300).display_user_balance()


print("\n")
#user make 3 deposits and 1 withdraw
print("Updated version:")
stig.make_deposit(2000).make_withdraw(800).make_withdraw(800).make_withdraw(300).display_user_balance()


print("\n")
print("Updated version:")
kahlil.transfer_money(stig, 100).display_user_balance()

stig.display_user_balance()

