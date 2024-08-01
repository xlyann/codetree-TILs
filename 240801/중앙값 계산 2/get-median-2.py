n = int(input())
_list = list(map(int, input().split()))
new = []
for i in range(n):
    new.append(_list[i])
    if i%2 == 0:
        new.sort()
        print(new[i//2], end = ' ')