class distance:
    def __init__(self, x, y, num):
        self.x, self.y, self.num = x, y, num

save = []
n = int(input())
for i in range(1, n+1):
    a, b = map(int, input().split())
    save.append(distance(a, b, i))

save.sort(key=lambda x:(abs(x.x)+abs(x.y), x.num))
for j in save:
    print(j.num)