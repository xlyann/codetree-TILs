n = int(input())
new = [[0]*n for _ in range(n)]
for j in range(n):
    new[0][j] = 1

for i in range(n):
    new[i][0] = 1

for i in range(1, n):
    for j in range(1, n):
        new[i][j] = new[i-1][j] + new[i][j-1] + new[i-1][j-1]

for row in new:
    for e in row:
        print(e, end = ' ')
    print()