n = int(input())
digit = []

while True:
    if n < 2:
        digit.append(n)
        break
    
    digit.append(n%2)
    n //= 2

for i in digit[::-1]:
    print(i, end = '')