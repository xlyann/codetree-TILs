a, b = map(int, input().split())
n = list(map(int, list(input())))
num_10 = 0

for i in n:
    num_10 = num_10*a + i

digit = []
while True:
    if num_10 < b:
        digit.append(num_10)
        break
    
    digit.append(num_10%b)
    num_10 //= b

for i in digit[::-1]:
    print(i, end = '')