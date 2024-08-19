# 남, 서, 북, 동 = 0, 1, 2, 3
dx, dy = [1, 0, -1, 0],[0, -1, 0, 1]
cnt = 0

n = int(input())
mirrors = [list(input()) for _ in range(n)]

def in_range(a, b):
    global n
    return 0<=a and a<n and 0<=b and b<n

def move_1(num):
    if num == 0 or num == 1:
        return 1-num
    if num == 2 or num == 3:
        return 5-num

def move_2(num):
    return 3-num

def move(a, b):
    if a == '/':
        return move_1(b)
    if a == '\\':
        return move_2(b)


lazer = int(input())
rotate = (lazer-1)//n
remain = (lazer-1)%n

if rotate == 0:
    x, y = 0, remain
elif rotate == 1:
    x, y = remain, n-1
elif rotate == 2:
    x, y = n-1, n-1-remain
else:
    x, y = n-1-remain, 0

while in_range(x, y):
    cnt += 1
    mirror = mirrors[x][y]
    rotate = move(mirror, rotate)
    x, y = x+dx[rotate], y+dy[rotate]

print(cnt)