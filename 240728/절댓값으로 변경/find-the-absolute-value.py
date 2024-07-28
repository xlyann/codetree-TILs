def _abs(num, _list):
    for i in range(num):
        if _list[i] < 0:
            _list[i] *= -1

a = int(input())
_list = list(map(int, input().split()))
_abs(a, _list)
print(*_list)