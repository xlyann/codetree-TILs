def ficonacci(n):
    if n == 1 or n == 2:
        return 1
    
    return ficonacci(n-1) + ficonacci(n-2)

a = int(input())
print(ficonacci(a))