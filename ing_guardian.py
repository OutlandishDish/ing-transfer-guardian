
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
    transactions = load_transactions()                  # load transactions using the load_transactions function from data_layer.py, which reads from the specified CSV file and returns a list of transaction dictionaries
    print(f"Loaded {len(transactions)} transactions.")  # print the number of transactions loaded for verification  
    print(transactions[:3])                             # print the first 3 transactions for a quick check of the data structure    

    status = check_transfer(transactions)
    notify(status)