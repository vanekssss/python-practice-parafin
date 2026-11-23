import csv


class ExpenseBook:
    def __init__(self, expenses=None):
        self.expenses = expenses if expenses is not None else []

    def __len__(self):
        return len(self.expenses)

    def __contains__(self, category):
        return any(expense["category"] == category for expense in self.expenses)

    def __iter__(self):
        return iter(self.expenses)

    def __getitem__(self, index):
        return self.expenses[index]

    def __add__(self, other):
        if not isinstance(other, ExpenseBook):
            return NotImplemented
        return ExpenseBook(self.expenses + other.expenses)

    def __str__(self):
        total = sum(float(expense["amount"]) for expense in self.expenses)
        return f"Книга витрат: {len(self)} записів, загальна сума {total:.2f} UAH"


def load_expenses(filename):
    with open(filename, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


if __name__ == "__main__":
    expenses = load_expenses("expenses.csv")
    first_half = ExpenseBook([e for e in expenses if int(e["date"].split("-")[2]) <= 15])
    second_half = ExpenseBook([e for e in expenses if int(e["date"].split("-")[2]) > 15])

    all_expenses = first_half + second_half

    print("Перша половина:", first_half)
    print("Друга половина:", second_half)
    print("Об'єднана книга:", all_expenses)
    print("Кількість записів:", len(all_expenses))
    print("Чи є категорія food:", "food" in all_expenses)
    print("Перший запис:", all_expenses[0])

    print("Перелік витрат:")
    for expense in all_expenses:
        print(expense["date"], expense["category"], expense["amount"], expense["currency"])
