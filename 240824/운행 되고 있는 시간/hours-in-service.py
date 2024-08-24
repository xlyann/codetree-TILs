n = int(input())
worktime = list(tuple(map(int,input().split())) for _ in range(n))

ans = 0
for i in range(n):
    arr = [0]*1001
    for j in range(n):
        if i == j:
            continue
        a, b = worktime[j]
        for k in range(a, b):
            arr[k] = 1
    cnt = arr.count(1)
    ans = max(ans, cnt)
print(ans)