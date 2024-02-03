import csv
import json

data =  open(f"./cleaned_data/transactions_remove_input_blockhash.json", "r").read()
data = json.loads(data)
print("Length of data :", len(data))


csv_file_path = "./transaction_data.csv"

field_names = [
    "blockNumber", "timeStamp", "hash", "nonce", "transactionIndex",
    "from", "to", "value", "gas", "gasPrice", "isError", "txreceipt_status",
    "contractAddress", "cumulativeGasUsed", "gasUsed", "confirmations",
    "methodId", "functionName"
]

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    for item in data:
        writer.writerow(item)

print(csv_file_path)
