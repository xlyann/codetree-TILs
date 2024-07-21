count = 65
n = int(input())
for i in range(n):
    for j in range(n):
        if i>j:
            print(' ', end = ' ')
        else:
            print(chr(count), end = ' ')
            count += 1
        if count == 91:
            count = 65
    print()