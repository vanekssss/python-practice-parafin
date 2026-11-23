import csv
from pathlib import Path


class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = float(amount)

    def monthly_cost(self):
        return self.amount


class RecurringExpense(Expense):
    def __init__(self, date, category, amount, times_per_month):
        super().__init__(date, category, amount)
        self.times_per_month = times_per_month

    def monthly_cost(self):
        return self.amount * self.times_per_month


class SharedExpense(Expense):
    def __init__(self, date, category, amount, people):
        super().__init__(date, category, amount)
        self.people = people

    def monthly_cost(self):
        return self.amount / self.people


class YearlyExpense(Expense):
    def monthly_cost(self):
        return self.amount / 12


file_path = Path(__file__).parent / "data" / "expenses.csv"
expenses = []

with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file, delimiter=";")

    for row in reader:
        category = row["category"]
        amount = float(row["amount"].replace(",", "."))
        date = row["date"]

        if category == "Transport":
            expenses.append(RecurringExpense(date, category, amount, 8))
        elif category == "Mobile":
            expenses.append(RecurringExpense(date, category, amount, 1))
        elif category in ("Housing", "Groceries"):
            expenses.append(SharedExpense(date, category, amount, 2))

expenses.append(YearlyExpense("2026-11-23", "Yearly subscription", 1200))

total = 0

for expense in expenses:
    cost = expense.monthly_cost()
    total += cost
    print(f"{expense.category}: {cost:.2f} UAH")

print(f"Total monthly cost including yearly subscription: {total:.2f} UAH")
