from collections import defaultdict
from datetime import datetime
from storage import load_expenses


def analytics_menu():

    while True:

        print("\n" + "=" * 50)
        print("              ANALYTICS")
        print("=" * 50)
        print("1. Total Spending")
        print("2. Category Summary")
        print("3. Monthly Comparison")
        print("4. Highest Expense")
        print("5. Lowest Expense")
        print("6. Back")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            total_spending()

        elif choice == "2":
            category_summary()

        elif choice == "3":
            monthly_comparison()

        elif choice == "4":
            highest_expense()

        elif choice == "5":
            lowest_expense()

        elif choice == "6":
            return

        else:
            print("\n❌ Invalid choice.")
            input("\nPress Enter to continue...")


def total_spending():

    rows = load_expenses()

    if len(rows) <= 1:
        print("\nNo expenses found.")
        input("\nPress Enter to continue...")
        return

    total = sum(float(row[3]) for row in rows[1:])
    total_expenses = len(rows) - 1
    average = total / total_expenses

    print("\n" + "=" * 50)
    print("            TOTAL SPENDING")
    print("=" * 50)

    print(f"💰 Total Spending : ₹{total:.2f}")
    print(f"🧾 Total Expenses : {total_expenses}")
    print(f"📊 Average Expense: ₹{average:.2f}")

    print("=" * 50)

    input("\nPress Enter to continue...")


def category_summary():

    rows = load_expenses()

    if len(rows) <= 1:
        print("\nNo expenses found.")
        input("\nPress Enter to continue...")
        return

    summary = defaultdict(float)
    grand_total = 0

    for row in rows[1:]:

        category = row[1]
        amount = float(row[3])

        summary[category] += amount
        grand_total += amount

    print("\n" + "=" * 60)
    print("                 CATEGORY SUMMARY")
    print("=" * 60)

    print(f"{'Category':<20}{'Amount':<15}{'Percentage'}")
    print("-" * 60)

    for category, total in summary.items():

        percentage = (total / grand_total) * 100

        print(
            f"{category:<20}"
            f"₹{total:<13.2f}"
            f"{percentage:.1f}%"
        )

    print("-" * 60)
    print(f"Total Categories : {len(summary)}")
    print(f"Total Spending   : ₹{grand_total:.2f}")
    print("=" * 60)

    input("\nPress Enter to continue...")
def monthly_comparison():

    rows = load_expenses()

    if len(rows) <= 1:
        print("\nNo expenses found.")
        input("\nPress Enter to continue...")
        return

    monthly_totals = defaultdict(float)

    for row in rows[1:]:

        date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
        month_key = date.strftime("%Y-%m")

        monthly_totals[month_key] += float(row[3])

    months = sorted(monthly_totals.keys())

    print("\n" + "=" * 60)
    print("               MONTHLY COMPARISON")
    print("=" * 60)

    if len(months) == 1:

        month = months[0]

        print(f"Month           : {month}")
        print(f"Total Spending  : ₹{monthly_totals[month]:.2f}")
        print("\nAdd expenses in another month to compare.")

        print("=" * 60)

        input("\nPress Enter to continue...")
        return

    current_month = months[-1]
    previous_month = months[-2]

    current_total = monthly_totals[current_month]
    previous_total = monthly_totals[previous_month]

    difference = current_total - previous_total

    print(f"Current Month   ({current_month}) : ₹{current_total:.2f}")
    print(f"Previous Month  ({previous_month}) : ₹{previous_total:.2f}")

    print("-" * 60)

    if previous_total > 0:
        percentage = (difference / previous_total) * 100

        print(f"Percentage Change : {percentage:+.2f}%")

    else:
        print("Percentage Change : N/A")

    if difference > 0:
        print(f"Difference        : +₹{difference:.2f}")
        print("Status            : Spending Increased 📈")

    elif difference < 0:
        print(f"Difference        : -₹{abs(difference):.2f}")
        print("Status            : Spending Decreased 📉")

    else:
        print("Difference        : ₹0.00")
        print("Status            : No Change")

    print("=" * 60)

    input("\nPress Enter to continue...")


def highest_expense():

    rows = load_expenses()

    if len(rows) <= 1:
        print("\nNo expenses found.")
        input("\nPress Enter to continue...")
        return

    highest = max(rows[1:], key=lambda row: float(row[3]))

    print("\n" + "=" * 60)
    print("               HIGHEST EXPENSE")
    print("=" * 60)

    print(f"Date & Time : {highest[0]}")
    print(f"Category    : {highest[1]}")
    print(f"Description : {highest[2]}")
    print(f"Amount      : ₹{float(highest[3]):.2f}")

    print("=" * 60)

    input("\nPress Enter to continue...")


def lowest_expense():

    rows = load_expenses()

    if len(rows) <= 1:
        print("\nNo expenses found.")
        input("\nPress Enter to continue...")
        return

    lowest = min(rows[1:], key=lambda row: float(row[3]))

    print("\n" + "=" * 60)
    print("                LOWEST EXPENSE")
    print("=" * 60)

    print(f"Date & Time : {lowest[0]}")
    print(f"Category    : {lowest[1]}")
    print(f"Description : {lowest[2]}")
    print(f"Amount      : ₹{float(lowest[3]):.2f}")

    print("=" * 60)

    input("\nPress Enter to continue...")