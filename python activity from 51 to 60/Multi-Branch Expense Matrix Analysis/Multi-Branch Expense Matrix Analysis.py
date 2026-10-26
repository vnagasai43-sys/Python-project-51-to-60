branches = int(input("Enter number of branches: "))
months = int(input("Enter number of months: "))

expenses = []

for i in range(branches):
    row = []
    for j in range(months):
        amount = float(input("Enter expense: "))
        row.append(amount)
    expenses.append(row)
for i in range(branches):
    total = sum(expenses[i])
    print("Branch", i + 1, "Total:", total)
    print("Average:", total / months)