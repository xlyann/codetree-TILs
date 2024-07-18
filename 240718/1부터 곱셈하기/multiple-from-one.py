prod = 1
n = int(input())
for i in range(1, 11):
    prod *= i
    if prod >= n:
        num = i
        break
print(num)