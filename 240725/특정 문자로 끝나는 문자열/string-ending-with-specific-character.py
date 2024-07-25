_list = list(input() for _ in range(10))
find = input()
count = 0
for i in _list:
    if i[-1] == find:
        print(i)
    else:
        count += 1

if count == 10:
    print('None')