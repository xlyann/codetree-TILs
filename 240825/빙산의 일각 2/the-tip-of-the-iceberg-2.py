n = int(input())
iceberg = list(int(input()) for _ in range(n))

ans = 0
for i in range(max(iceberg)):
    cnt = 0
    first = 0
    for j in iceberg:
        last = j
        if first <= i and last > i:
            cnt += 1
        first = j
    ans = max(ans, cnt)
print(ans)