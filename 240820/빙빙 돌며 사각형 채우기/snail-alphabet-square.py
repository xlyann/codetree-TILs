dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
dir_num = 0
n, m = map(int, input().split())
answer = [[0]*m for _ in range(n)]


def in_range(a, b):
    global n, m
    return 0<=a and a<n and 0<=b and b<m

answer[x][y] = 'A'
alpha_num = 66

for i in range(2, n*m+1):
    if alpha_num == 91:
        alpha_num = 65

    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num+1)%4
    
    x, y = x + dx[dir_num], y + dy[dir_num]
    answer[x][y] = chr(alpha_num)
    alpha_num += 1

for i in range(n):
    for j in range(m):
        print(answer[i][j], end = ' ')
    print()