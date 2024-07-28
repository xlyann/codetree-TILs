def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def even_sum(num):
    new = list(map(int, list(str(num))))
    if sum(new)%2 == 0:
        return True
    return False

def find_range(a, b):
    count = 0
    for i in range(a, b+1):
        if is_prime(i) and even_sum(i):
            count += 1
    return count

a, b = map(int, input().split())
print(find_range(a, b))