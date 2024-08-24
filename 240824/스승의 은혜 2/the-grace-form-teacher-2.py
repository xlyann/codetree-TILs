n, money = map(int, input().split())
gift = list(int(input()) for _ in range(n))
gift.sort()

ans = 0
for i in range(n):
    save = money
    cnt = 0
    for j in range(n):
        if i == j:
            save -= gift[j]//2
        else:
            save -= gift[j]
        if save < 0:
            break
        else:
            cnt += 1
    ans = max(ans, cnt)
print(ans)