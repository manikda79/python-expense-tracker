import csv
from datetime import datetime

from storage import (
    load_expenses,
    save_expenses,
    csv_exists
)

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

    rows = load_expenses()

    if not rows:
        rows.append([
            "Date & Time",
            "Category",
            "Description",
            "Amount"
        ])

    rows.append([
        current_datetime,
        category,
        description,
        amount
    ])

    save_expenses(rows)

    print("\n✅ Expense Added Successfully!")
    input("\nPress Enter to continue...")


def view_expenses():

    print("\n========== ALL EXPENSES ==========\n")

    if not csv_exists():
        print("No expenses found.")
        input("\nPress Enter to continue...")
        return

    rows = load_expenses()

    if len(rows) <= 1:
        print("No expenses found.")
        input("\nPress Enter to continue...")
        return

    print(f"{'No':<5}{'Date & Time':<22}{'Category':<18}{'Description':<25}{'Amount'}")
    print("-" * 85)

    for index, row in enumerate(rows[1:], start=1):
        print(
            f"{index:<5}"
            f"{row[0]:<22}"
            f"{row[1]:<18}"
            f"{row[2]:<25}"
            f"₹{float(row[3]):.2f}"
        )

    print("-" * 85)
    print(f"Total Expenses : {len(rows)-1}")

    input("\nPress Enter to continue...")


def search_expense():

    if not csv_exists():
        print("\nNo expenses found.")
        input("\nPress Enter to continue...")
        return

    rows = load_expenses()

    while True:

        print("\n========== SEARCH ==========")
        print("1. Search by Category")
        print("2. Search by Description")
        print("3. Back")

        choice = input("\nEnter choice: ")

        if choice == "1":

            keyword = input("\nEnter Category: ").strip().lower()

            found = False

            print("\nResults\n")

            for row in rows[1:]:

                if keyword == row[1].lower():

                    print(
                        f"{row[0]} | {row[1]} | {row[2]} | ₹{float(row[3]):.2f}"
                    )

                    found = True

            if not found:
                print("No matching expenses found.")

            input("\nPress Enter to continue...")

        elif choice == "2":

            keyword = input("\nEnter Description: ").strip().lower()

            found = False

            print("\nResults\n")

            for row in rows[1:]:

                if keyword in row[2].lower():

                    print(
                        f"{row[0]} | {row[1]} | {row[2]} | ₹{float(row[3]):.2f}"
                    )

                    found = True

            if not found:
                print("No matching expenses found.")

            input("\nPress Enter to continue...")

        elif choice == "3":
            return

        else:
            print("\nInvalid Choice.")


def delete_expense():

    if not csv_exists():
        print("\nNo expenses found.")
        input("\nPress Enter to continue...")
        return

    rows = load_expenses()

    if len(rows) <= 1:
        print("\nNo expenses found.")
        input("\nPress Enter to continue...")
        return

    print("\n========== DELETE EXPENSE ==========\n")

    print(f"{'No':<5}{'Category':<18}{'Description':<25}{'Amount'}")
    print("-" * 60)

    for index, row in enumerate(rows[1:], start=1):

        print(
            f"{index:<5}"
            f"{row[1]:<18}"
            f"{row[2]:<25}"
            f"₹{float(row[3]):.2f}"
        )

    while True:

        try:

            choice = int(input("\nEnter expense number to delete (0 to cancel): "))

            if choice == 0:
                return

            if 1 <= choice <= len(rows) - 1:

                deleted = rows.pop(choice)

                save_expenses(rows)

                print("\n✅ Expense Deleted Successfully!")
                print(f"Deleted: {deleted[2]} - ₹{float(deleted[3]):.2f}")

                break

            else:
                print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")

    input("\nPress Enter to continue...")