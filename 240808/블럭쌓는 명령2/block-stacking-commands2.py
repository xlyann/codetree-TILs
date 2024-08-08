N, K = map(int, input().split())
block = [0]*N
for j in range(K):
    init, final = map(int, input().split())
    for i in range(init, final + 1):
        block[i-1] += 1

print(max(block))