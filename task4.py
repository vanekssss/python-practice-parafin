class Expense:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category

    def balance_change(self):
        return -self.amount


class Income:
    def __init__(self, amount, source):
        self.amount = amount
        self.source = source

    def balance_change(self):
        return self.amount


class Transfer:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

    def balance_change(self):
        return 0


def main():
    print("Ivan Parafin, IT-32")

    operations = [
        Income(2600.00, "стипендія"),
        Income(850.00, "підробіток"),
        Expense(145.50, "food"),
        Expense(32.00, "transport"),
        Expense(286.40, "groceries"),
        Expense(150.00, "mobile"),
        Expense(98.00, "food"),
        Expense(40.00, "transport"),
        Expense(412.75, "groceries"),
        Expense(180.00, "entertainment"),
        Expense(125.00, "food"),
        Expense(32.00, "transport"),
        Expense(220.00, "education"),
        Expense(365.30, "groceries"),
        Transfer(500.00, "переказ між власними картками")
    ]

    income_total = 0
    expenses_total = 0
    transfers_total = 0
    balance = 0

    for operation in operations:
        change = operation.balance_change()
        balance += change

        if isinstance(operation, Income):
            income_total += change
        elif isinstance(operation, Expense):
            expenses_total += change
        else:
            transfers_total += change

    print(f"income:    {income_total:9.2f}")
    print(f"expenses:  {expenses_total:9.2f}")
    print(f"transfers: {transfers_total:9.2f}")
    print(f"balance:   {balance:9.2f}")


if __name__ == "__main__":
    main()
