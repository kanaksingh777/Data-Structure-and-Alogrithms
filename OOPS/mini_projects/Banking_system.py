

#flake8: noqa
#13:33
class Account:
    def __init__(self,account_number,account_holder):

        self.account_number = account_number
        self.account_holder = account_holder 
        self.balance = 0

    
    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount

        else: raise ValueError("Insufficient Balance")

    def get_details(self):
        return {'account_number':self.account_number ,'account_holder': self.account_holder, 'balance':self.balance}


class SavingsAccount(Account):
    def __init__(self,account_number,account_holder,interest_rate):
        super().__init__(account_number,account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):

        interest = self.interest_rate * self.balance
        self.balance = self.balance + interest

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self,account:Account):
        self.accounts[account.account_number]=account

    def find_account(self,account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_details()

    
        