def onjeon(num):
    if num%2 == 0:
        return False

    if num%10 == 5:
        return False
    
    if num%3 == 0 and num%9 != 0:
        return False

    return True

def onjeon_range(a, b):
    count = 0
    for i in range(a, b+1):
        if onjeon(i):
            count += 1
    return count

a, b = map(int, input().split())
print(onjeon_range(a, b))