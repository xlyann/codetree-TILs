memo = [0]
def list_max(n):
    if n < len(memo):
        return memo[n]
    if n == 1:
        memo.append(_list[0])
        return _list[0]
    
    if _list[n-1] < list_max(n-1):
        memo.append(list_max(n-1))
    else:
        memo.append(_list[n-1])
    
    return list_max(n-1)

a = int(input())
_list = list(map(int, input().split()))
print(list_max(a))