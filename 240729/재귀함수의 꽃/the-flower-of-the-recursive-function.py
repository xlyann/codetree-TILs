def symmetry(n):
    if n == 0:
        return
    
    print(n, end = ' ')
    symmetry(n-1)
    print(n, end = ' ')

a = int(input())
symmetry(a)