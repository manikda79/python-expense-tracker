import csv
import os

CSV_FILE = "data/expenses.csv"


def load_expenses():
    """
    Load all expenses from the CSV file.
    Returns a list of rows including the header.
    """

    if not os.path.exists(CSV_FILE):
        return []

    with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)


def save_expenses(rows):
    """
    Save all rows back to the CSV file.
    """

    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def csv_exists():
    """
    Check whether the CSV file exists.
    """

    return os.path.exists(CSV_FILE)