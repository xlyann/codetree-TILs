dy, dx = [1, 0, 0, -1], [0, 1, -1, 0]
mapper = {'R':0, 'D':1, 'U':2, 'L':3}

n, t = map(int, input().split())
x, y, rotate = input().split()
x, y = int(x)-1, int(y)-1
dir_num = mapper[rotate]

def in_range(a, b):
    global n
    return 0<=a and a<n and 0<=b and b<n

for _ in range(t):
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if not in_range(nx, ny):
        dir_num = 3 - dir_num
    else:
        x, y = nx, ny

print(x+1, y+1)