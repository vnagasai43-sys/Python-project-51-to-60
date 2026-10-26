capacity = int(input("Enter bus capacity: "))
stops = int(input("Enter number of stops: "))
passengers = 0

for i in range(1, stops + 1):
    board = int(input("Passengers boarding: "))
    leave = int(input("Passengers getting down: "))

    passengers = passengers + board - leave

    print("Passengers:", passengers)

    if passengers > capacity:
        print("Bus is overloaded")
    else:
        print("Capacity is OK")