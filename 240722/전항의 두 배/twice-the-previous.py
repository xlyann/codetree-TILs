num = list(map(int, input().split()))
for i in range(1, 9):
    num.append(2*num[i-1]+num[i])
print(*num)