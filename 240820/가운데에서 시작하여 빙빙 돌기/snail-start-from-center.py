dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0
n = int(input())
answer = [[0]*n for _ in range(n)]
x, y = (n-1)//2, (n-1)//2

answer[x][y] = 1
move = 1
distance = 0
cnt = 0

for i in range(2, n*n+1):
    x, y = x + dx[dir_num], y + dy[dir_num]
    answer[x][y] = i
    distance += 1

    if distance == move:
        dir_num = (dir_num+3)%4
        distance = 0
        cnt += 1
    
    if cnt == 2:
        cnt = 0
        move += 1    

for i in range(n):
    for j in range(n):
        print(answer[i][j], end = ' ')
    print()