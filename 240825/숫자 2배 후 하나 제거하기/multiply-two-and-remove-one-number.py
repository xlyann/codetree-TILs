n = int(input())
num = list(map(int, input().split()))

ans = 99999999
for i in range(n):
    num[i] *= 2
    for j in range(n):
        remain_num = [elem for k, elem in enumerate(num) if j != k]
        sum_diff = 0
        for l in range(n-2):
            sum_diff += abs(remain_num[l] - remain_num[l+1])
        ans = min(sum_diff, ans)
    num[i] //= 2
print(ans)