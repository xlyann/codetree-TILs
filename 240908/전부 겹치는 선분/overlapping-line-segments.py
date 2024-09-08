n = int(input())
line = list(tuple(map(int, input().split())) for _ in range(n))

ans = 0
for i in range(1, 101):
    overlap = True
    for a, b in line:
        if i < a or b < i:
            overlap = False
    if overlap:
        ans = 1

if ans == 1:
    print('Yes')
else:
    print('No')