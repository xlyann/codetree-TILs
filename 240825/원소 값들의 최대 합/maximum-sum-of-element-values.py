n, times = map(int, input().split())
num = list(map(int, input().split()))

ans = 0
for i in range(n):
    sum_val = 0
    target = i
    for j in range(times):
        sum_val += num[target-1]
        target = num[target-1]
    ans = max(ans, sum_val)
print(ans)