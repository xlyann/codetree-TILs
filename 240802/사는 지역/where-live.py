class live:
    def __init__(self, name, num, location):
        self.name = name
        self.num = num
        self.location = location

save = []
n = int(input())
for i in range(n):
    a, b, c = input().split()
    save.append(live(a, b, c))

vs = []
for i in save:
    new = i.name
    vs.append(new)

vs.sort()
need = vs[-1]

for i in range(n):
    new = save[i].name
    if new == need:
        find = i
        break

print('name', save[find].name)
print('addr', save[find].num)
print('city', save[find].location)