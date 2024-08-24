n, x, y = map(int, input().split())
point_s = []
point_n = []

for _ in range(n):
    a, b = input().split()
    if a == 'S':
        point_s.append(int(b))
    if a == 'N':
        point_n.append(int(b))

ans = 0
for i in range(x, y+1):
    min_s = 9999999
    min_n = 9999999
    for point in point_s:
        min_s = min(min_s, abs(point-i))
    for point in point_n:
        min_n = min(min_n, abs(point-i))
    if min_s<=min_n:
        ans += 1
print(ans)