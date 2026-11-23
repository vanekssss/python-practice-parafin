import csv
from pathlib import Path


class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Owner can not be empty")
        if balance < 0:
            raise ValueError("Balance can not be negative")

        self.owner = owner.strip()
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance can not be negative")
        self.__balance = round(value, 2)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Not enough money")
        self.__balance = round(self.__balance - amount, 2)


budget = float(input("Enter your real monthly budget (UAH): "))
wallet = Wallet("Ivan Parafin", budget)

file_path = Path(__file__).parent / "data" / "expenses.csv"

with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file, delimiter=";")

    required_columns = {"category", "amount", "comment"}
    if not required_columns.issubset(reader.fieldnames or []):
        raise ValueError(
            "CSV must have columns: category;amount;comment. "
            "Adjust the names in task4.py if your Lab 22 file uses other headers."
        )

    for row in reader:
        category = row["category"]
        amount = float(row["amount"].replace(",", "."))
        comment = row["comment"]

        try:
            wallet.withdraw(amount)
            print(f"{category}: -{amount:.2f} UAH ({comment})")
        except ValueError:
            print(f"Not enough money for: {category} ({amount:.2f} UAH)")
            break

print("Owner:", wallet.owner)
print(f"Remaining balance: {wallet.balance:.2f} UAH")
