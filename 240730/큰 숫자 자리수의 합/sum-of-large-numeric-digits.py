def sum_num(n):
    if n < 10:
        return n
    
    return sum_num(n//10) + n%10

def multi(a, b, c):
    return a*b*c

def f(a, b, c):
    new = multi(a, b, c)
    return sum_num(new)

a, b, c = map(int, input().split())
print(f(a, b, c))