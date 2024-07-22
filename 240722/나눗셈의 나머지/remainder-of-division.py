a, b = map(int, input().split())
num = [0]*b
while a>1:
    num[a%b] += 1
    a //= b

sum_val = 0
for i in num:
    sum_val += i*i

print(sum_val)