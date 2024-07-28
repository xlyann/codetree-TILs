def swap(n, m):
    return m, n
a, b = map(int, input().split())
a, b = swap(a, b)
print(a, b)