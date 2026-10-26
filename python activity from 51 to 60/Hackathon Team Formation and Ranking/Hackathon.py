teams = []
n = int(input("Enter number of teams: "))
for i in range(n):
    name = input("Enter team name: ")
    r1 = int(input("Enter round 1 score: "))
    r2 = int(input("Enter round 2 score: "))
    total = r1 + r2
    teams.append((name, total))
for team in teams:
    print(team[0], "Total:", team[1])
best = teams[0]
for team in teams:
    if team[1] > best[1]:
        best = team
print("Winner:", best[0])
print("Total score:", best[1])