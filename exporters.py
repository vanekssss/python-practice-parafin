from abc import ABC, abstractmethod
from pathlib import Path
import csv
import json
from html import escape


class Exporter(ABC):
    @abstractmethod
    def export(self, expenses, path):
        """Write expenses to the file at path."""

    def target(self, name):
        return Path(f"{name}.{self.extension()}")

    @abstractmethod
    def extension(self):
        """Return file extension without dot."""


class CsvExporter(Exporter):
    def extension(self):
        return "csv"

    def export(self, expenses, path):
        path = Path(path)
        expenses = list(expenses)
        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "category", "amount", "currency"])
            writer.writeheader()
            writer.writerows(expenses)


class JsonExporter(Exporter):
    def extension(self):
        return "json"

    def export(self, expenses, path):
        with Path(path).open("w", encoding="utf-8") as file:
            json.dump(list(expenses), file, ensure_ascii=False, indent=4)


class TxtExporter(Exporter):
    def extension(self):
        return "txt"

    def export(self, expenses, path):
        expenses = list(expenses)
        lines = [
            "DATE        CATEGORY       AMOUNT      CURRENCY",
            "-" * 55
        ]
        for item in expenses:
            lines.append(
                f"{item['date']:<11} {item['category']:<14} "
                f"{float(item['amount']):>8.2f}      {item['currency']}"
            )
        Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


class HtmlExporter(Exporter):
    def extension(self):
        return "html"

    def export(self, expenses, path):
        rows = []
        for item in expenses:
            rows.append(
                "<tr>"
                f"<td>{escape(str(item['date']))}</td>"
                f"<td>{escape(str(item['category']))}</td>"
                f"<td>{float(item['amount']):.2f}</td>"
                f"<td>{escape(str(item['currency']))}</td>"
                "</tr>"
            )

        document = """<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<title>Звіт витрат</title>
<style>
body { font-family: Arial, sans-serif; margin: 35px; background: #f4f6f8; }
h1 { color: #243b53; }
table { border-collapse: collapse; width: 100%; background: white; }
th, td { border: 1px solid #cbd2d9; padding: 10px; text-align: left; }
th { background: #d9eaf7; }
tr:nth-child(even) { background: #f0f4f8; }
</style>
</head>
<body>
<h1>Звіт витрат — Парафін Іван, ІТ-32</h1>
<table>
<thead><tr><th>Дата</th><th>Категорія</th><th>Сума</th><th>Валюта</th></tr></thead>
<tbody>
""" + "\n".join(rows) + """
</tbody>
</table>
</body>
</html>
"""
        Path(path).write_text(document, encoding="utf-8")


try:
    Exporter()
except TypeError as error:
    print("error:", error)
