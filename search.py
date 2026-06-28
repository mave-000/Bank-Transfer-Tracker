import csv
import os

CSV_FILE = "Transactions_To.csv"

def load_transactions():
    # Check if CSV exists before trying to open it
    if not os.path.exists(CSV_FILE):
        print("\nError: Transactions file not found.")
        print("Please run extract.py first to generate the CSV.\n")
        exit()

    transactions = []
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            transactions.append(row)

    if not transactions:
        print("\nError: CSV file is empty. Re-run extract.py.\n")
        exit()

    return transactions

def search_transfers(transactions, name):
    name_lower = name.lower()
    matches = [t for t in transactions if name_lower in t["Description"].lower()]

    if not matches:
        print(f"\nNo transfers found matching '{name}'.\n")
        return

    # Handle missing or invalid amount values safely
    total = 0
    for t in matches:
        try:
            total += float(t["Amount"])
        except (ValueError, TypeError):
            pass

    print(f"\nResults for '{name}':")
    print(f"Transactions : {len(matches)}")
    print(f"Total amount : ₦{total:,.2f}\n")

# Run
transactions = load_transactions()
print(f"Loaded {len(transactions)} transactions.\n")

while True:
    name = input("Enter name to search (or 'quit' to exit): ").strip()
    if name.lower() == "quit":
        break
    if name:
        search_transfers(transactions, name)