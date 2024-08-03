class length:
    def __init__(self, l, num):
        self.l, self.num = l, num

save = []
n = int(input())
_list = list(map(int, input().split()))

for i in range(1, n+1):
    save.append(length(_list[i-1], i))

save.sort(key=lambda x:(x.l, x.num))


new = [0]*(n+1)
for j, rank in enumerate(save, start = 1):
    new[rank.num] = j
print(*new[1:])