def gcd(m,n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)

def lcm(m,n):
    return m*n//gcd(m,n)

a, b = map(int, input().split())
print(gcd(a,b), lcm(a,b))