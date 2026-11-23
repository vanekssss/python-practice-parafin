import csv
from exporters import CsvExporter, JsonExporter, TxtExporter


def load_expenses(path):
    with open(path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


if __name__ == "__main__":
    expenses = load_expenses("expenses.csv")
    print("Parafin Ivan, IT-32")

    exporters = [CsvExporter(), JsonExporter(), TxtExporter()]
    for exporter in exporters:
        path = exporter.target("report")
        exporter.export(expenses, path)
        print(f"saved: {path} ({len(expenses)} records)")
