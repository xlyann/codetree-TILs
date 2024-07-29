def string_sq(n):
    if n < 10:
        return n**2
    
    return string_sq(n//10) + (n%10)**2

a = int(input())
print(string_sq(a))