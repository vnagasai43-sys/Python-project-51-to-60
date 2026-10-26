routes = int(input("Enter number of routes: "))
capacity = int(input("Enter bus capacity: "))

for i in range(1, routes + 1):
    passengers = int(input("Enter passengers for route: "))

    if capacity <= 0:
        print("Invalid bus capacity")
    else:
        buses = passengers // capacity

        if passengers % capacity != 0:
            buses += 1

        print("Route:", i)
        print("Buses needed:", buses)