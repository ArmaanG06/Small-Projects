def budget_tracker():
    while True:
        budget = float(input("Enter your starting budget: $"))
        balance = budget

        while balance > 0:
            expense = float(input("Enter expense amount: $"))
            description = input("Enter expense description: ")
            balance -= expense
            print(f"Expense recorded: {description} - ${expense:.2f}")
            print(f"Remaining balance: ${balance:.2f}")

            if balance < 0:
                while balance < 0:
                    print(f"Over budget by ${-balance:.2f}. Please add more funds to balance the books.")
                    additional_funds = float(input("Enter additional funds: $"))
                    balance += additional_funds
                    print(f"New balance: ${balance:.2f}")
            
        print("Budget depleted. Restarting the tracker...\n")

budget_tracker()
