n = int(input())
for i in range(n):
    prod = 1
    a, b = map(int, input().split())
    for j in range(a, b+1):
        prod *= j
    print(prod)