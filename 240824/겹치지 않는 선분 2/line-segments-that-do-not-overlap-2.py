n = int(input())
point = list(tuple(map(int, input().split())) for _ in range(n))

ans = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        a, b = point[i]
        c, d = point[j]
        if (a<c and b<d) or (a>c and b>d):
            cnt += 1

    if cnt == n-1:
        ans += 1
print(ans)