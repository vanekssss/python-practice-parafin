from datetime import datetime
import json
from pathlib import Path


class Expense:
    currency = "UAH"
    created_count = 0

    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment
        Expense.created_count += 1

    @staticmethod
    def is_valid_date(text):
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_amount(value):
        try:
            return float(value) >= 0
        except (ValueError, TypeError):
            return False

    @classmethod
    def from_csv_line(cls, line):
        parts = line.strip().split(";", 3)
        if len(parts) != 4:
            print(f"Пропущено некоректний CSV-рядок: {line.strip()}")
            return None

        date, category, amount, comment = parts

        if not cls.is_valid_date(date) or not cls.is_valid_amount(amount):
            print(f"Пропущено некоректний CSV-рядок: {line.strip()}")
            return None

        return cls(date, category, float(amount), comment)

    @classmethod
    def from_dict(cls, data):
        date = data.get("date", "")
        category = data.get("category", "")
        amount = data.get("amount")
        comment = data.get("comment", "")

        if not cls.is_valid_date(date) or not cls.is_valid_amount(amount):
            print(f"Пропущено некоректний JSON-запис: {data}")
            return None

        return cls(date, category, float(amount), comment)

    @classmethod
    def from_input(cls):
        date = input("Дата (YYYY-MM-DD): ")
        category = input("Категорія: ")
        amount = input("Сума: ")
        comment = input("Коментар: ")

        if not cls.is_valid_date(date) or not cls.is_valid_amount(amount):
            print("Помилка: неправильна дата або сума.")
            return None

        return cls(date, category, float(amount), comment)

    @classmethod
    def set_currency(cls, code):
        cls.currency = code

    def show(self):
        print(
            f"{self.date} | {self.category:<14} | "
            f"{self.amount:8.2f} {self.currency} | {self.comment}"
        )


def load_csv(path):
    result = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            expense = Expense.from_csv_line(line)
            if expense is not None:
                result.append(expense)
    return result


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    result = []
    for item in data:
        expense = Expense.from_dict(item)
        if expense is not None:
            result.append(expense)
    return result


def main():
    print("Ivan Parafin, IT-32")
    folder = Path(__file__).resolve().parent / "data"

    csv_expenses = load_csv(folder / "expenses.csv")
    json_expenses = load_json(folder / "expenses.json")

    print("\nВитрати, завантажені з CSV:")
    for expense in csv_expenses:
        expense.show()

    print("\nВитрати, завантажені з JSON:")
    for expense in json_expenses:
        expense.show()

    print("\nПорівняння:")
    print(f"Кількість з CSV: {len(csv_expenses)}")
    print(f"Кількість з JSON: {len(json_expenses)}")
    print(f"Дані однакові: {len(csv_expenses) == len(json_expenses)}")

    birthday = Expense.from_dict({
        "date": "2009-07-07",
        "category": "birthday",
        "amount": 0,
        "comment": "дата народження"
    })
    print("\nПерсональні дані:")
    print(f"Дата народження: {birthday.date}")

    print("\nПеревірка статичних методів:")
    print(Expense.is_valid_date("2026-02-30"))
    print(Expense.is_valid_amount("125.50"))

    Expense.set_currency("UAH")
    print(f"\nВалюта для всіх об'єктів: {Expense.currency}")
    print(f"Створено об'єктів: {Expense.created_count}")


if __name__ == "__main__":
    main()
