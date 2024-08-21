n = int(input())
num_list = [int(input()) for _ in range(n)]
max_sum = 0

def carry(a, b, c):
    new = a+b+c
    if new%10 == a%10 + b%10 + c%10:
        for i in range(1, 5):
            limit = 10**i
            if not new//limit == a//limit + b//limit + c//limit:
                return 0
        return 1
    return 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            a, b, c = num_list[i], num_list[j], num_list[k]
            if carry(a, b, c):
                sum_val = a+b+c
                max_sum = max(max_sum, sum_val)

print(max_sum)