count = 1
n = int(input())
for i in range(n): 
    for j in range(n):
        print(count, end="")
        count += 1
        if count == 10:
            count = 1
    print()