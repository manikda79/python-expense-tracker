"""
Smart Expense Tracker
Track. Analyze. Improve.

Author: Manikanta Elaprolu
Version: 1.0.0
"""


def show_welcome():
    print("=" * 50)
    print("        SMART EXPENSE TRACKER")
    print("         Track. Analyze. Improve.")
    print("=" * 50)


def show_main_menu():
    print("\n========== MAIN MENU ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Analytics")
    print("6. Settings")
    print("7. Exit")


def show_analytics_menu():
    print("\n========== ANALYTICS ==========")
    print("1. Total Spending")
    print("2. Monthly Comparison")
    print("3. Category Analysis")
    print("4. Average Daily Spending")
    print("5. Spending Trend")
    print("6. Back")


def show_settings_menu():
    print("\n========== SETTINGS ==========")
    print("1. Monthly Budget")
    print("2. Currency")
    print("3. Export Data")
    print("4. About")
    print("5. Back")


def main():
    show_welcome()

    while True:
        show_main_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\n🚧 Add Expense - Coming Soon")

        elif choice == "2":
            print("\n🚧 View Expenses - Coming Soon")

        elif choice == "3":
            print("\n🚧 Search Expense - Coming Soon")

        elif choice == "4":
            print("\n🚧 Delete Expense - Coming Soon")

        elif choice == "5":
            show_analytics_menu()
            input("\nPress Enter to return to Main Menu...")

        elif choice == "6":
            show_settings_menu()
            input("\nPress Enter to return to Main Menu...")

        elif choice == "7":
            print("\nThank you for using Smart Expense Tracker!")
            break

        else:
            print("\n❌ Invalid choice.")
            input("Press Enter to try again...")


if __name__ == "__main__":
    main()