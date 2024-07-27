def gcd(n, m):
    if n<m:
        n, m = m, n
    if m == 0:
        return n
    
    return gcd(m, n%m)

def lcm(m,n):
    return m*n//gcd(m,n)

a, b = map(int, input().split())
print(lcm(a, b))