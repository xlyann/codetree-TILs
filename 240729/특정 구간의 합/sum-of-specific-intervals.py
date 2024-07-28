length, times = map(int, input().split())
_list = list(map(int, input().split()))

def sum_list(a, b):
    global _list
    return sum(_list[a-1:b])

for i in range(times):
    a, b = map(int, input().split())
    print(sum_list(a, b))