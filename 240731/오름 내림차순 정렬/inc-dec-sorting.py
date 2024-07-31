a = int(input())
_list = list(map(int, input().split()))
_list.sort()

print(*_list)
print(*_list[::-1])