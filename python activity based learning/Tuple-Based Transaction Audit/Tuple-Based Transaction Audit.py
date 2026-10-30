transactions = []
n = int(input("Enter number of transactions: "))
for i in range(n):
    tid = input("Enter transaction ID: ")
    amount = float(input("Enter amount: "))
    kind = input("Enter deposit or withdrawal: ")
    transactions.append((tid, amount, kind))
seen = []
for t in transactions:
    tid, amount, kind = t
    if tid in seen:
        print("Duplicate ID:", tid)
    else:
        seen.append(tid)
    if amount <= 0:
        print("Invalid amount:", tid)
    if kind != "deposit" and kind != "withdrawal":
        print("Invalid transaction type:", tid)
print("Transaction checking completed")