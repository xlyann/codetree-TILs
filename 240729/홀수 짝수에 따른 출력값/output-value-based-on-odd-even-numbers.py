def sum_even_odd(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return sum_even_odd(n-2) + n

a = int(input())
print(sum_even_odd(a))