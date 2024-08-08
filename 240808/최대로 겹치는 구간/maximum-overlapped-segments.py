n = int(input())
_list = list(tuple(map(int, input().split())) for _ in range(n))

line = [0] * 201
for a, b in _list:
    for i in range(a+100, b+100):
        line[i] += 1

print(max(line))