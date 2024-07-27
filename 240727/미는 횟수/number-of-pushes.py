target = input()
find = input()

count = 0
while True:
    if target == find:
        break
    count += 1
    find = find[1:] + find[0]

    if count > len(target):
        count = -1
        break

print(count)