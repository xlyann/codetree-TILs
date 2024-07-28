def f(a, b):
    if a>b:
        return a+25, b*2
    return a*2, b+25

a, b = map(int, input().split())
a, b = f(a, b)
print(a, b)