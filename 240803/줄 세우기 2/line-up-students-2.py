class line:
    def __init__(self, height, weight, number):
        self.height, self.weight, self.number = height, weight, number

save = []
n = int(input())
for i in range(1, n+1):
    a, b = map(int, input().split())
    save.append(line(a, b, i))

save.sort(key=lambda x:(x.height, -x.weight))

for j in save:
    print(j.height, j.weight, j.number)