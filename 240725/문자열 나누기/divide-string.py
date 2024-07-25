n = int(input())
a = list(input().split())
new = ''
for i in a:
    new += i

count = 0
for i in new:
    print(i, end = '')
    count += 1
    if count == 5:
        print()
        count = 0