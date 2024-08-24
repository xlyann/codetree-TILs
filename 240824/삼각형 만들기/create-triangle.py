n = int(input())
point = list(tuple(map(int,input().split())) for _ in range(n))

def area(a, b):
    x_distance = max(a)-min(a)
    y_distance = max(b)-min(b)
    return x_distance*y_distance

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x1, y1 = point[i]
            x2, y2 = point[j]
            x3, y3 = point[k]
            x_point = {x1, x2, x3}
            y_point = {y1, y2, y3}
            if len(x_point)==2 and len(y_point)==2:
                val = area(x_point, y_point)
                ans = max(ans, val)
print(ans)