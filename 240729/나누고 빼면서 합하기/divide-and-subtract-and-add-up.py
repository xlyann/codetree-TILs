def f(num):
    if num %2 == 0:
        return num//2
    return num-1

def sum_list(num):
    sum_val = 0
    while num != 0:
        sum_val += _list[num-1]
        num = f(num)
    return sum_val

a, b = map(int, input().split())
_list = list(map(int, input().split()))

print(sum_list(b))