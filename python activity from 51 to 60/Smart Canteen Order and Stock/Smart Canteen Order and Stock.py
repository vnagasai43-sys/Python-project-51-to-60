items = ["Idli", "Dosa", "Juice"]
prices = [20, 40, 25]
stock = [30, 20, 15]
sales = 0
for i in range(3):
    print(i + 1, items[i], "Rs.", prices[i])
n = int(input("Enter number of orders: "))
for i in range(n):
    choice = int(input("Choose item (1-3): "))
    qty = int(input("Enter quantity: "))
    if choice < 1 or choice > 3:
        print("Invalid item")
    elif qty <= 0:
        print("Invalid quantity")
    elif qty > stock[choice - 1]:
        print("Not enough stock")
    else:
        bill = prices[choice - 1] * qty
        stock[choice - 1] -= qty
        sales += bill
        print("Bill: Rs.", bill)
print("Total sales: Rs.", sales)
print("Remaining stock:", stock)