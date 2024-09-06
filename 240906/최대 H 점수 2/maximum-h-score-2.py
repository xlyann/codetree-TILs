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
    if cnt >= i or (i-cnt <= l and cnt_1 >= l):
        ans = i
    else:
        print(ans)
        break