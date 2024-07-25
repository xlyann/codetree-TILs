target = input()
find = input()
cut = len(find)
count = 0
for i in range(len(target)-cut+2):
    if target[i:i+cut] == find:
        count += 1
print(count)