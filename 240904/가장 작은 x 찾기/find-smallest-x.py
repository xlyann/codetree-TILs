n = int(input())
give = list(tuple(map(int, input().split())) for _ in range(n))

def right(n):
    n *= 2
    for a, b in give:
        if a<=n and n<=b:
            n *= 2
            continue
        return False
    return True

find = 1
while True:
    if right(find):
        ans = find
        break
    find += 1
print(ans)