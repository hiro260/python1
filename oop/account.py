class Account(object):

    account_number = 0

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.id = Account.account_number
        Account.account_number += 1
    
    def withdraw(self, balance, amount):
        if balance >= amount:
            balance = balance - amount
        else:
            print("no withdraw because not enough balance") 
        return balance

    def deposite(self, balance, amount):
        balance = balance + amount
        return balance


#print(Account.account_number)
account_hiro = Account(1000, "Hiro")
#print(Account.account_number)
account_naoko = Account(0, "Naoko")
#print(Account.account_number)
account_yuki = Account(3000, "Yuki")
#print(Account.account_number)
account_saki = Account(5000, "Yuki")
#print(Account.account_number)

print(account_yuki.balance)
print(account_yuki.name)
print(account_yuki.id)

account_yuki.balance = account_yuki.withdraw(account_yuki.balance, 1300)
print(account_yuki.balance)

account_yuki.balance = account_hiro.deposite(account_yuki.balance, 1000)
print(account_yuki.balance)