n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if i%2 == 0:
        b.insert(0, i)
print(*b)