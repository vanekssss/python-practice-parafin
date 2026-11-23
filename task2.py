class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Owner can not be empty")
        if balance < 0:
            raise ValueError("Balance can not be negative")

        self.owner = owner.strip()
        self.__balance = round(balance, 2)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance = round(self.__balance + amount, 2)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Not enough money")
        self.__balance = round(self.__balance - amount, 2)


wallet = Wallet("Ivan Parafin", 1500)
wallet.deposit(500)
wallet.withdraw(200)

print("Owner:", wallet.owner)
print("Balance through name mangling:", wallet._Wallet__balance)

try:
    print(wallet.__balance)
except AttributeError as error:
    print("Error:", error)
