class Account(object):

    def __init__(self, balance):
        self._balance = balance
        self.show_balance()

    def deposite(self, price):
        self._balance += price

    def withdraw(self, price):
        if self._balance < price:
            print('you do not have enough amount')
        else:
            self._balance -= price
            self.show_balance()

    def show_balance(self):
        print(f"balance is {self._balance}.")

myaccount = Account(10000)
#print(dir(myaccount))

print(myaccount._balance)