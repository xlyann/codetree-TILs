class f:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

save = []
n = int(input())
for i in range(n):
    a, b, c = input().split()
    save.append(f(a, int(b), int(c)))

save.sort(key=lambda x:(x.height, -x.weight))
for j in save:
    print(j.name, j.height, j.weight)