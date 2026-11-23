class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not value.strip():
            raise ValueError("Owner can not be empty")
        self.__owner = value.strip()

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance can not be negative")
        self.__balance = round(value, 2)

    @property
    def is_empty(self):
        return self.__balance == 0


wallet = Wallet("Ivan Parafin", 1500)

print("Owner:", wallet.owner)
print("Balance:", wallet.balance)
print("Is empty:", wallet.is_empty)

wallet.balance = 1200.555
print("New balance:", wallet.balance)

try:
    wallet.balance = -100
except ValueError as error:
    print("Error:", error)

try:
    wallet.is_empty = True
except AttributeError as error:
    print("Error:", error)
