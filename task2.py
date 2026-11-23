import csv
from task1 import Money


def load_expenses(filename):
    items = []
    with open(filename, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            items.append({
                "date": row["date"],
                "category": row["category"],
                "money": Money(float(row["amount"]), row["currency"])
            })
    return items


if __name__ == "__main__":
    expenses = load_expenses("expenses.csv")
    amounts = [item["money"] for item in expenses]

    print("Витрати за зростанням:")
    for amount in sorted(amounts):
        print(amount)

    total = sum(amounts, Money(0))
    print("Загальна сума:", total)

    try:
        print(Money(10) + 5)
    except TypeError as error:
        print("TypeError:", error)
