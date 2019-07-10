# Define Bank Account Below:
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
    
    def deposit(self, num):
        self.balance += num
        return self.balance
        
    def withdraw(self, num):
        self.balance -= num
        return self.balance
