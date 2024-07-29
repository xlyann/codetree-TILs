def sum_range_1(n):
    if n == 1:
        return 1
    
    return sum_range_1(n-1) + n

a = int(input())
print(sum_range_1(a))