n, k = map(int, input().split())
num = list(int(input()) for _ in range(n))

ans = 0
for i in range(1, 10000-k+1):
    cnt = 0
    for j in num:
        if i<=j and j<=i+k:
            cnt += 1
    ans = max(ans, cnt)
print(ans)