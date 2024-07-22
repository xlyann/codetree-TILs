n = int(input())
num = list(map(int, input().split()))
new = [0]*(max(num)+1)
for i in num:
    new[i] += 1

if not 1 in new:
    print(-1)
else:
    for j in range(len(new)-1, 0, -1):
        if new[j] == 1:
            print(j)
            break