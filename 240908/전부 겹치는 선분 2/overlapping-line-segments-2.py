n = int(input())
line = list(tuple(map(int, input().split())) for _ in range(n))

overlap = False
for i in range(n):
    max_x1 = 0
    min_x2 = float('inf')
    for j in range(n):
        if i == j:
            continue
        x1, x2 = line[j][0], line[j][1]
        max_x1 = max(max_x1, x1)
        min_x2 = min(min_x2, x2)
    if max_x1 < min_x2:
        overlap = True

if overlap:
    print('Yes')
else:
    print('No')