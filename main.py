import finance

def show_menu():
    """Display the application menu and return the user's choice."""
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Records")
    print("4. Exit")
    return input("Enter your choice: ")

def main():
    while True:
        choice = show_menu()
        if choice == "1":
            date = input("Enter the date (MM/DD/YY): ")
            category = input("Enter what for: ")
            amount = input("Enter the amount: ")
            finance.add_record(date, "Income", category, amount)
        elif choice == "2":
            date = input("Enter the date (MM/DD/YY): ")
            category = input("Enter what for: ")
            amount = input("Enter the amount: ")
            finance.add_record(date, "Expense", category, amount)
        elif choice == "3":
            finance.read_records()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
