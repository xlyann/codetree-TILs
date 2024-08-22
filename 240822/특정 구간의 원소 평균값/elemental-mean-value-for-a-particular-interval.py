n = int(input())
num = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i, n):
        cnt = 0
        sum_val = 0
        save = []
        for k in range(i, j+1):
            cnt += 1
            sum_val += num[k]
            save.append(num[k])
        average = sum_val/cnt
        if save.count(average) >= 1:
            ans+=1
print(ans)