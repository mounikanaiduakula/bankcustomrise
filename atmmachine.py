# Predefined accounts as list of dictionaries
accounts = [
    {"name": "Alice", "pin": "1111", "balance": 1000, "transactions": ["account opened with $1000"]},
    {"name": "Bob", "pin": "2222", "balance": 1500, "transactions": ["account opened with $1500"]},
    {"name": "Charlie", "pin": "3333", "balance": 2000, "transactions": ["account opened with $2000"]},
    {"name": "David", "pin": "4444", "balance": 2500, "transactions": ["account opened with $2500"]},
    {"name": "Eva", "pin": "5555", "balance": 3000, "transactions": ["account opened with $3000"]},
    {"name": "Frank", "pin": "6666", "balance": 3500, "transactions": ["account opened with $3500"]},
    {"name": "Grace", "pin": "7777", "balance": 4000, "transactions": ["account opened with $4000"]},
    {"name": "Hannah", "pin": "8888", "balance": 4500, "transactions": ["account opened with $4500"]},
    {"name": "Ian", "pin": "9999", "balance": 5000, "transactions": ["account opened with $5000"]},
    {"name": "Jane", "pin": "0000", "balance": 5500, "transactions": ["account opened with $5500"]}
]

# Function to check balance
def check_balance(name, pin):
    for account in accounts:
        if account["name"] == name and account["pin"] == pin:
            print(f"Your balance is ₹{account['balance']}")
            return
    print("Invalid name or PIN")

# Function to deposit money
def deposit(name, pin, amount):
    for account in accounts:
        if account["name"] == name and account["pin"] == pin:
            account["balance"] += amount
            account["transactions"].append(f"Deposited ₹{amount}")
            print(f"Deposit successful! New balance: ₹{account['balance']}")
            return
    print("Invalid name or PIN")

# Function to withdraw money
def withdraw(name, pin, amount):
    for account in accounts:
        if account["name"] == name and account["pin"] == pin:
            if account["balance"] >= amount:
                account["balance"] -= amount
                account["transactions"].append(f"Withdrew ₹{amount}")
                print(f"Withdrawal successful! New balance: ₹{account['balance']}")
            else:
                print("Insufficient balance")
            return
    print("Invalid name or PIN")

# Function to show transaction history
def show_transactions(name, pin):
    for account in accounts:
        if account["name"] == name and account["pin"] == pin:
            if account["transactions"]:
                print("\n--- Transaction History ---")
                for txn in account["transactions"]:
                    print(txn)
            else:
                print("No transactions found.")
            return
    print("Invalid name or PIN")

# ATM Menu
while True:
    print("\n==== ATM MENU ====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        pin = input("Enter your PIN: ")
        check_balance(name, pin)

    elif choice == "2":
        name = input("Enter your name: ")
        pin = input("Enter your PIN: ")
        amount = float(input("Enter deposit amount: "))
        deposit(name, pin, amount)

    elif choice == "3":
        name = input("Enter your name: ")
        pin = input("Enter your PIN: ")
        amount = float(input("Enter withdrawal amount: "))
        withdraw(name, pin, amount)

    elif choice == "4":
        name = input("Enter your name: ")
        pin = input("Enter your PIN: ")
        show_transactions(name, pin)

    elif choice == "5":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
