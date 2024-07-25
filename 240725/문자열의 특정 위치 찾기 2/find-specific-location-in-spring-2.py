_list = ["apple", "banana", "grape", "blueberry", "orange"]
count = 0
find = input()
for i in _list:
    if i[2] == find or i[3] == find:
        count += 1
        print(i)
print(count)