def rec(a, b):
    for i in range(a):
        print('1'*b)

n, m = map(int, input().split())
rec(n, m)