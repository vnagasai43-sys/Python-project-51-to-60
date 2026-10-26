n = int(input("Enter number of books: "))
total_fine = 0

for i in range(n):
    book = input("Enter book ID: ")
    days = int(input("Enter late days: "))

    fine = days * 2
    total_fine += fine

    print("Book ID:", book)
    print("Fine: Rs.", fine)

    if days > 0:
        print("Book is overdue")
    else:
        print("Book returned on time")

print("Total fine: Rs.", total_fine)