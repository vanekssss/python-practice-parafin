import csv
import sys
from exporters import CsvExporter, JsonExporter, TxtExporter, HtmlExporter


def load_expenses(path):
    with open(path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def main():
    available = {
        "csv": CsvExporter(),
        "json": JsonExporter(),
        "txt": TxtExporter(),
        "html": HtmlExporter()
    }

    if len(sys.argv) != 2 or sys.argv[1] not in available:
        print("Доступні формати:", ", ".join(available))
        return 2

    extension = sys.argv[1]
    exporter = available[extension]
    expenses = load_expenses("expenses.csv")
    path = exporter.target("report")
    exporter.export(expenses, path)
    print(f"saved: {path} ({len(expenses)} records)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
