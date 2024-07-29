def asc(n):
    if n == 0:
        return
    
    asc(n-1)
    print(n, end = ' ')

def desc(n):
    if n == 0:
        return
    
    print(n, end = ' ')
    desc(n-1)

a = int(input())
asc(a)
print()
desc(a)