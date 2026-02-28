
from data_layer import load_transactions

def check_transfer(transactions):
    # placeholder logic for now
    return False

def notify(status):
    if status:
        print("Transfer successful.")
    else:
        print("Transfer missing.")

if __name__ == "__main__":
    csv_path = r"D:\Coding\Python\ing_csvs\transactions.csv"
    transactions = load_transactions(csv_path)

    status = check_transfer(transactions)
    notify(status)