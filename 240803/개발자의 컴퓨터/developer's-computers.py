n = int(input())
new = {}
for i in range(n):
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i in new:
            new[i] += c
        else:
            new[i] = c

num = 0
for j in new.values():
    if num < j:
        num = j
print(num)