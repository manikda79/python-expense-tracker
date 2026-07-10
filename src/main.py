
from expense_manager import (
    add_expense,
    view_expenses,
    search_expense,
    edit_expense,
    delete_expense,
)

from expense_analytics import analytics_menu
from storage import load_expenses
from collections import defaultdict
from datetime import datetime


def show_dashboard():

    rows = load_expenses()

    total_expenses = 0
    total_spending = 0
    top_category = "N/A"

    if len(rows) > 1:

        total_expenses = len(rows) - 1

        total_spending = sum(float(row[3]) for row in rows[1:])

        category_totals = defaultdict(float)

        for row in rows[1:]:
            category_totals[row[1]] += float(row[3])

        top_category = max(
            category_totals,
            key=category_totals.get
        )

    print("=" * 60)
    print("              SMART EXPENSE TRACKER")
    print("               Track. Analyze. Improve.")
    print("=" * 60)

    print()

    print(f"📅 Date            : {datetime.now().strftime('%Y-%m-%d')}")

    print(f"🧾 Total Expenses  : {total_expenses}")

    print(f"💰 Total Spending  : ₹{total_spending:.2f}")

    print(f"🏆 Top Category    : {top_category}")

    print()

    print("=" * 60)


def show_main_menu():
    print("\n========== MAIN MENU ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Edit Expense")
    print("5. Delete Expense")
    print("6. Analytics")
    print("7. Exit")



def main():

    show_dashboard()

    while True:

        show_main_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_expense()

        elif choice == "4":
            edit_expense()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            analytics_menu()

        elif choice == "7":
            print("\nThank you for using Smart Expense Tracker!")
            print("Have a great day! 👋")
            break

        else:
            print("\n❌ Invalid Choice.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()