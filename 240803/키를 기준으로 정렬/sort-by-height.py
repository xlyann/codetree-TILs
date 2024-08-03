class student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

save = []
n = int(input())
for i in range(n):
    a, b, c = input().split()
    b = int(b)
    save.append(student(a, b, c))

save.sort(key=lambda x: x.height)

for j in save:
    print(j.name, j.height, j.weight)