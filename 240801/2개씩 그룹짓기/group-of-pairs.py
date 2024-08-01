n = int(input())
_list = list(map(int, input().split()))
_list.sort()
max_val = 0
for i in range(n):
    new = _list[i] + _list[-i-1]
    if new>max_val:
        max_val = new
print(max_val)