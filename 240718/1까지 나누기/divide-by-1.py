count = 0
n = int(input())
for i in range(1, 11):
    n //= i
    count += 1
    if n <= 1:
        break
print(count)