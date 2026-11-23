import csv
from abc import ABC, abstractmethod
from pathlib import Path
from exporters import Exporter, HtmlExporter


class IncompleteHtmlExporter(Exporter):
    def extension(self):
        return "html"


try:
    IncompleteHtmlExporter()
except TypeError as error:
    print("До реалізації export():", error)


def load_expenses(path):
    with open(path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


if __name__ == "__main__":
    expenses = load_expenses("expenses.csv")
    exporter = HtmlExporter()
    path = exporter.target("report")
    exporter.export(expenses, path)
    print(f"saved: {path} ({len(expenses)} records)")
    print("Відкрийте report.html у браузері.")
