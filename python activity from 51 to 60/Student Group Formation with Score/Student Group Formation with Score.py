scores = []

n = int(input("Enter number of students: "))

for i in range(n):
    mark = int(input("Enter student score: "))
    scores.append(mark)

size = int(input("Enter group size: "))

if size <= 0:
    print("Invalid group size")
else:
    group = 1

    for i in range(0, n, size):
        print("Group", group, ":", scores[i:i + size])
        group = group + 1