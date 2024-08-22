n, times, height = map(int, input().split())
ground = list(map(int, input().split()))

ans = 999999
for i in range(n-times+1):
    sum_val = 0
    for j in range(i, i+times):
        sum_val += abs(ground[j]-height)
    ans = min(ans, sum_val)
print(ans)