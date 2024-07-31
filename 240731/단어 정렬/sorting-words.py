a = int(input())
_list = [input() for _ in range(a)]
_list.sort()
print('\n'.join(_list))