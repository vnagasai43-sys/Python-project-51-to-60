products = int(input("Enter number of products: "))
batches = int(input("Enter number of batches: "))
limit = float(input("Enter defect percentage limit: "))
for i in range(1, products + 1):
    for j in range(1, batches + 1):
        made = int(input("Enter units produced: "))
        defective = int(input("Enter defective units: "))
        if made > 0:
            percent = defective * 100 / made
        else:
            percent = 0
        print("Product:", i, "Batch:", j)
        print("Defect percentage:", round(percent, 2), "%")
        if percent > limit:
            print("Quality check needed")
        else:
            print("Quality is acceptable")