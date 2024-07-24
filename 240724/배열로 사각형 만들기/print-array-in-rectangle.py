new = [[0]*5 for _ in range(5)]
for j in range(5):
    new[0][j] = 1

for i in range(5):
    new[i][0] = 1

for i in range(1, 5):
    for j in range(1, 5):
        new[i][j] = new[i-1][j] + new[i][j-1]

for row in new:
    for e in row:
        print(e, end = ' ')
    print()