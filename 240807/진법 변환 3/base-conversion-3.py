n = list(map(int, list(input())))
num_10 = 0

for i in n:
    num_10 = num_10*8 + i

digit = []
while True:
    if num_10 < 2:
        digit.append(num_10)
        break
    
    digit.append(num_10%2)
    num_10 //= 2

for i in digit[::-1]:
    print(i, end = '')