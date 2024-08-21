dx, dy = [], []
a, b = map(int, input().split())
arr = [list(input()) for _ in range(a)]
cnt = 0

def in_range(x, y):
    global a, b
    return 0 <= x and x < a and 0 <= y and y < b

dxs, dys = [1, 1, 1, -1, -1, -1, 0, 0], [-1, 0, 1, -1, 0, 1, -1, 1]

for i in range(a): 
    for j in range(b):
        if arr[i][j] != 'L':
            continue
        for dx, dy in zip(dxs, dys):
            curt = 0
            curx = i
            cury = j
            for _ in range(2):
                nx = curx + dx
                ny = cury + dy
                if in_range(nx, ny) == False:
                    break
                if arr[nx][ny] != 'E':
                    break
                curt += 1
                curx = nx
                cury = ny
			
                if curt == 2:
                    cnt += 1

print(cnt)