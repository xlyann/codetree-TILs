c1, t1 = input().split()
c2, t2 = input().split()
c3, t3 = input().split()

def A(a, b):
    if a == 'Y' and int(b) >= 37:
        return 1
    return 0

count = A(c1, t1) + A(c2, t2) + A(c3, t3)
 
print('E' if count>=2 else 'N')