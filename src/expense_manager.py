import csv
import os
from datetime import datetime

CSV_FILE = "data/expenses.csv"

CATEGORIES = [
    "Food",
    "Transport",
    "Shopping",
    "Health",
    "Entertainment",
    "Education",
    "Bills",
    "Other"
]


def add_expense():

    print("\n========== ADD EXPENSE ==========")

    print("\nChoose Category:")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")

    while True:
        try:
            category_choice = int(input("\nEnter category number: "))

            if 1 <= category_choice <= len(CATEGORIES):
                category = CATEGORIES[category_choice - 1]
                break

            print("Invalid category.")

        except ValueError:
            print("Please enter a number.")

    description = input("Enter Description: ")

    while True:

        try:
            amount = float(input("Enter Amount: ₹"))
            break

        except ValueError:
            print("Please enter a valid amount.")

    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date & Time",
                "Category",
                "Description",
                "Amount"
            ])

        writer.writerow([
            current_datetime,
            category,
            description,
            amount
        ])

    print("\n✅ Expense Added Successfully!")

    input("\nPress Enter to continue...")


def view_expenses():
    print("\n🚧 View Expenses - Coming Soon")
    input("\nPress Enter to continue...")


def search_expense():
    print("\n🚧 Search Expense - Coming Soon")
    input("\nPress Enter to continue...")


def delete_expense():
    print("\n🚧 Delete Expense - Coming Soon")
    input("\nPress Enter to continue...")