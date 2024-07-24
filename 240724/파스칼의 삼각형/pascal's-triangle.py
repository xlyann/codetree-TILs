n = int(input())
new = [[0]*n for _ in range(n)]

for i in range(n):
    new[i][0] = 1

for i in range(1, n):
    for j in range(1, n):
        new[i][j] = new[i-1][j] + new[i-1][j-1]
    
for row in new:
    for e in row:
        if e == 0:
            break
        print(e, end = ' ')
    print()