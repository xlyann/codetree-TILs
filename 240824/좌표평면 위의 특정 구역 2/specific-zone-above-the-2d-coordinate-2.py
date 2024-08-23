n = int(input())
point = list(tuple(map(int, input().split())) for _ in range(n))

ans = 40001*40001
for i in range(n):
    x_min = 40001
    x_max = 0
    y_min = 40001
    y_max = 0
    for j in range(n):
        if i == j:
            continue
        x, y = point[j]
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)
    area = (x_max-x_min)*(y_max-y_min)
    ans = min(ans, area)
print(ans)