def list_max(n):
    if n == 1:
        return _list[0]
    
    if _list[n-1] > list_max(n-1):
        best = _list[n-1]
    else:
        best = list_max(n-1)

    return best

a = int(input())
_list = list(map(int, input().split()))
print(list_max(a))