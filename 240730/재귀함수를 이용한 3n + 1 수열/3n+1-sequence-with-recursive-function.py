def f(n):
    if n == 1:
        return 0
    if n%2 == 0:
        n //= 2
    else:
        n = 3*n+1
    
    return f(n)+1

a = int(input())
print(f(a))