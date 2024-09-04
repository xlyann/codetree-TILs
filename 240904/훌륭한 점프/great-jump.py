n,k = map(int, input().split())
num = list(map(int, input().split()))

def possible(n):
    global k
    stone = []
    for i, elem in enumerate(num):
        if elem<=n:
            stone.append(i)

    for j in range(1, len(stone)):
        dist = stone[j] - stone[j-1]
        if dist>k:
            return False
    return True

ans = 101
for i in range(n, min(num[0], num[-1]), -1):
    if possible(i):
        ans = min(ans, i)
        
print(ans)