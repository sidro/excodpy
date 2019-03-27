class BankAccount(object):
<<<<<<< HEAD

=======
    #global balance
    balance = 0
>>>>>>> 35741eacd0d09a3c0632de450c3f5630b20527cb

    def __init__(self, initial_balance):
        self.balance = initial_balance

    def depozit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def overdrawn(self):
        return self.balance < 0

    def bal(self):
        return self.balance


def main():
    my_account = BankAccount(15)
    my_account.withdraw(5)
    print(my_account.bal())


if __name__ == "__main__":
    main()
