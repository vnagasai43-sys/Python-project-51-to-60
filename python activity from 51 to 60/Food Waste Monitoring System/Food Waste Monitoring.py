days = int(input("Enter number of days: "))

for i in range(1, days + 1):
    made = int(input("Meals prepared: "))
    served = int(input("Meals served: "))

    waste = made - served

    if made > 0:
        percent = waste * 100 / made
    else:
        percent = 0

    print("Food waste:", waste)
    print("Waste percentage:", round(percent, 2), "%")

    if percent > 10:
        print("High food waste")
    else:
        print("Food waste is acceptable")