dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 3

n, times = map(int, input().split())
command = list(input())
number = [list(map(int, input().split())) for _ in range(n)]
x, y = (n-1)//2, (n-1)//2
sum_val = number[x][y]

def in_range(a, b):
    global n
    return 0<=a and a<n and 0<=b and b<n

for i in command:
    if i == 'L':
        dir_num = (dir_num+3)%4
    if i == 'R':
        dir_num = (dir_num+1)%4
    if i == 'F':
        nx, ny = x+dx[dir_num], y+dy[dir_num]
        if in_range(nx, ny):
            x, y = nx, ny
            sum_val += number[x][y]

print(sum_val)