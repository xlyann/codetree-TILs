N, K = map(int, input().split())
block = [0]*N
for _ in range(K):
    init, final = map(int, input().split())
    for i in range(init, final + 1):
        block[i] += 1

max_val = 0
for h in block:
    if h>max_val:
        max_val = h

print(max_val)