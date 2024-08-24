n, k = map(int, input().split())
bomb = list(int(input()) for _ in range(n))

ans = -1
for i in range(n):
    for j in range(i-k, i+k):
        if 0 <= j and j<=n-1 and i != j and bomb[j] == bomb[i]:
            ans = max(ans, bomb[j])
print(ans)