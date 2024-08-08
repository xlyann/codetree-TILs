N, K = map(int, input().split())
block = [0]*(N+1)
for j in range(K):
    init, final = map(int, input().split())
    for i in range(init, final + 1):
        block[i] += 1

print(max(block))