n = int(input())
_list = list(input() for _ in range(n))
find = input()

count = 0
length = 0
for i in _list:
    if i[0] == find:
        count += 1
        length += len(i)

print(count, f'{length/count:.2f}')