class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __del__(self):
        print(f"wallet of {self.owner} deleted")


print("First example")
wallet = Wallet("Ivan Parafin", 1500)
del wallet

print("\nSecond example")
wallet = Wallet("Ivan Parafin", 1500)
other = wallet
del wallet
print("The other reference still exists")
del other

print("\nThird example")
wallet = Wallet("Ivan Parafin", 2000)
print("End of program")
