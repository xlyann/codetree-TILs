n, m = map(int, input().split())
new = [[0]*n for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())
    new[r-1][c-1] = 1

for row in new:
    for e in row:
        print(e, end = ' ')
    print()