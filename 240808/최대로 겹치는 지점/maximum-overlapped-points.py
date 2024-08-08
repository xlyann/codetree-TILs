n = int(input())
_list = list(tuple(map(int, input().split())) for _ in range(n))

line = [0] * 101
for a, b in _list:
    for i in range(a, b+1):
        line[i] += 1

print(max(line))