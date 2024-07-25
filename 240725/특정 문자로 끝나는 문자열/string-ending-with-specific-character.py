_list = list(input() for _ in range(10))
find = input()
for i in _list:
    if i[-1] == find:
        print(i)