n = int(input())
cow = list(input())
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cow[i] + cow[j] + cow[k] == 'COW':
                cnt += 1
print(cnt)