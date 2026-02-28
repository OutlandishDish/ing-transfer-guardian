
import csv
from datetime import datetime

def load_transactions(csv_path):
    transactions = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            credit = row["Credit"].strip()
            debit = row["Debit"].strip()

            if credit:
                amount = float(credit)
                tx_type = "credit"
            else:
                amount = -float(debit)
                tx_type = "debit"

            transactions.append({
                "date": datetime.strptime(row["Date"], "%d/%m/%Y"),
                "description": row["Description"].strip().lower(),
                "amount": amount,
                "type": tx_type
            })
    return transactions