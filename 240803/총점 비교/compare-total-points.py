class score:
    def __init__(self, name, a, b, c):
        self.name, self.a, self.b, self.c = name, a, b, c

save = []
n = int(input())
for i in range(n):
    a, b, c, d = input().split()
    save.append(score(a, int(b), int(c), int(d)))

save.sort(key=lambda x: x.a + x.b + x.c)
for j in save:
    print(j.name, j.a, j.b, j.c)