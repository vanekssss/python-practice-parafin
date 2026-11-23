class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Owner can not be empty")

        if balance < 0:
            raise ValueError("Balance can not be negative")

        self.owner = owner.strip()
        self.balance = round(balance, 2)


wallet = Wallet("Ivan Parafin", 1500)
print("Owner:", wallet.owner)
print("Balance:", wallet.balance)

try:
    wallet1 = Wallet("", 500)
except ValueError as error:
    print("Error:", error)

try:
    wallet2 = Wallet("Ivan Parafin", -100)
except ValueError as error:
    print("Error:", error)
