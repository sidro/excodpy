class BankAccount(object):

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
