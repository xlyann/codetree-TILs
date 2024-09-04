n, m = map(int, input().split())
num_list = list(tuple(map(int, input().split())) for _ in range(m))

ans = 0
for i in range(1, n):
    for j in range(i, n+1):
        cnt = 0
        for a, b in num_list:
            if (i == a and j == b) or (i == b and j == a):
                cnt += 1
        ans = max(ans, cnt)
print(ans)