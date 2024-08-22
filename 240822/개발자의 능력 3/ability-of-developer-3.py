num = list(map(int, input().split()))
ans = 99999

for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            sum_val = num[i] + num[j] + num[k]
            less = sum(num)-sum_val
            ans = min(ans, abs(sum_val-less))
print(ans)