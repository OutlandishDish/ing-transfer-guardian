
from pathlib import Path                            
import csv
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent                          # get the directory of the current script (data_layer.py) to construct the path to transactions.csv
CSV_PATH = BASE_DIR / "data" / "transactions.csv"                   # define the path to the transactions.csv file relative to the current script

def load_transactions(csv_path=CSV_PATH):                           # load transactions from the specified CSV file path, defaulting to the constructed CSV_PATH    
    transactions = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            credit = row["Credit"].strip()
            debit = row["Debit"].strip()

            if credit:                               # if credit is not empty, it's a credit transaction
                amount = float(credit)              # if credit is not empty, it's a credit transaction
                tx_type = "credit"                  # if credit is not empty, it's a credit transaction
            else:
                amount = -float(debit)              # if debit is not empty, it's a debit transaction (negative amount)
                tx_type = "debit"                   # if debit is not empty, it's a debit transaction (negative amount)

            transactions.append({                                                   # create a transaction dictionary for each row
                "date": datetime.strptime(row["Date"], "%d/%m/%Y"),                 # convert date string to datetime object
                "description": row["Description"].strip().lower(),                  # convert description to lowercase for easier matching
                "amount": amount,                                                   # use the calculated amount (positive for credit, negative for debit)
                "type": tx_type                                                     # add the transaction type (credit or debit) to the dictionary
            })
    return transactions