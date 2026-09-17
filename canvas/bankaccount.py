class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if isinstance(amount, (int, float)) and amount >= 0:
            self._balance = amount
        else:
            raise ValueError("Balance must be a positive number or zero.")


account = BankAccount("John", 5000)

print(account.balance)

account.balance = 7500

print(account.balance)