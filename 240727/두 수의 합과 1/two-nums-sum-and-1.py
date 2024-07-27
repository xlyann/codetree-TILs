a, b = map(int, input().split())
find_1 = str(a+b)

count = 0
for i in find_1:
    if i == '1':
        count += 1
print(count)