count = 65
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(count), end = '')
        count += 1
    print()