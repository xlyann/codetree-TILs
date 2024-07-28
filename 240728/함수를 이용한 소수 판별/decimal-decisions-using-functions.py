def prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    if num == 1:
        return False
    return True

def prime_sum(a, b):
    sum_val = 0
    for i in range(a, b+1):
        if prime(i):
            sum_val += i
    return sum_val

a, b = map(int, input().split())
print(prime_sum(a, b))