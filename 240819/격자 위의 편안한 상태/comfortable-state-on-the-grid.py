dx, dy = [0, 1, 0, -1],[1, 0, -1, 0]
n, m = map(int, input().split())
color = [[0]*n for _ in range(n)]

def in_range(a, b):
    global n
    return 0<=a and a<n and 0<=b and b<n

def comfortable(x, y):
    global dx, dy
    cnt = 0
    for elem1, elem2 in zip(dx, dy):
        nx, ny = x+elem1, y+elem2
        if in_range(nx, ny) and color[nx][ny] == 1:
            cnt += 1
    
    if cnt == 3:
        return print(1)
    return print(0)

for i in range(m):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    color[x][y] = 1
    comfortable(x, y)