def even(num, _list):
    for i in range(num):
        if _list[i]%2 == 0:
            _list[i] //= 2

a = int(input())
num = list(map(int, input().split()))
even(a, num)
print(*num)