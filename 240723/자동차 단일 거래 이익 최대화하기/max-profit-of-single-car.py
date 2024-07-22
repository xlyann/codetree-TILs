a = int(input())
num = list(map(int, input().split()))
_max = 0
for i in range(a):
    if max(num[i:]) - num[i] > _max:
        _max = max(num[i:]) - num[i]
print(_max)