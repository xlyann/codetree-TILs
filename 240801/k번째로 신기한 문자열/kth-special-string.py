n, k, save = input().split()
_list = [input() for _ in range(int(n))]
new = []

for i in _list:
    if i.startswith(save):
        new.append(i)

new.sort()
print(new[int(k)-1])