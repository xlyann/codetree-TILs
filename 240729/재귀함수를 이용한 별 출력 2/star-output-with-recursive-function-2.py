def symmetry_stars(n):
    if n == 0:
        return
    
    print('* '*n)
    symmetry_stars(n-1)
    print('* '*n)

a = int(input())
symmetry_stars(a)