import csv
from task1 import Money
from task3 import ExpenseBook

BUDGET = Money(3000)


def load_expenses(filename):
    with open(filename, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


class BudgetExpenseBook(ExpenseBook):
    def __gt__(self, budget):
        if not isinstance(budget, Money):
            return NotImplemented
        total = sum(
            (Money(float(expense["amount"]), expense["currency"]) for expense in self.expenses),
            Money(0)
        )
        if total.currency != budget.currency:
            raise ValueError("different currencies")
        return total.cents > budget.cents


if __name__ == "__main__":
    expenses = load_expenses("expenses.csv")
    book = BudgetExpenseBook(expenses)

    total = sum(
        (Money(float(expense["amount"]), expense["currency"]) for expense in book),
        Money(0)
    )

    print("Загальна сума витрат:", total)
    print("Місячний бюджет:", BUDGET)
    if book > BUDGET:
        print("Бюджет перевищено.")
    else:
        print("Витрати не перевищують бюджет.")
