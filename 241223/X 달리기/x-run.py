meter = int(input())
start = 1

for i in range(1, 100):
    if meter < i*i:
        value = i-1
        break

if meter == value**2:
    print(2*value-1)
else:
    print(value*2)