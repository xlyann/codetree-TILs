n, l = map(int, input().split())
num = list(map(int, input().split()))

for i in range(1, n+1):
    cnt = 0
    cnt_1 = 0
    for j in num:
        if i <= j:
            cnt += 1
        if i-j == 1:
            cnt_1 += 1
    if cnt >= i or (cnt+cnt_1>=i and cnt_1 <= l):
        ans = i
print(ans)