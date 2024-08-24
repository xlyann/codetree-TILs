n = int(input())
swap = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(1, n+1):
    start = [0]*(n+1)
    start[i] = 1
    cnt = 0
    for a, b, open_cup in swap:
        start[a], start[b] = start[b], start[a]
        if start[open_cup] == 1:
            cnt += 1
    ans = max(ans, cnt)
print(ans)