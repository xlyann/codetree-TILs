num = list(map(int, input().split()))
for i in range(2, 10):
    new = (num[i-1] + num[i-2])%10
    num.append(new)
print(*num)