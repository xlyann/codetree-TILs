a, b = map(int, input().split())
num = list(map(int, input().split()))
ans = 99999999

sum_val = sum(num)

for i in range(a):
    for j in range(i+1, a):
        new = sum_val - num[i] - num[j]
        ans = min(ans, abs(b-new))

print(ans)