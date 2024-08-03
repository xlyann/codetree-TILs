class personal:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

save = []
for i in range(5):
    a, b, c = input().split()
    save.append(personal(a, int(b), c))

save.sort(key=lambda x:x.name)
print('name')
for j in save:
    print(j.name, j.height, j.weight)
print()

save.sort(key=lambda x:-x.height)
print('height')
for j in save:
    print(j.name, j.height, j.weight)