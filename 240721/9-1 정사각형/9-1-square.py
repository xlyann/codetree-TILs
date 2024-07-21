count = 9
n = int(input())
for i in range(n): 
    for j in range(n):
        print(count, end="")
        count -= 1
        if count == 0:
            count = 9
    print()