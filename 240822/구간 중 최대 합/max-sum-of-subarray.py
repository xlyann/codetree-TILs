n, k = map(int, input().split())
num = list(map(int, input().split()))

ans = 0
for i in range(n-k+1):
    sum_val = 0
    for j in range(i, i+k):
        sum_val += num[j]
    ans = max(ans, sum_val)
print(ans)