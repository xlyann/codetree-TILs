dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
n = int(input())
cnt = 0
_list = list(list(map(int, input().split())) for _ in range(n))

def in_range(a, b):
    global n
    return 0<=a and a<n and 0<=b and b<n

for i in range(n):
    for j in range(n):
        cnt_1 = 0
        for elem1, elem2 in zip(dx, dy):
            nx, ny = i + elem1, j + elem2
            if in_range(nx, ny) and _list[nx][ny] == 1:
                cnt_1 += 1
        if cnt_1>=3:
            cnt += 1

print(cnt)