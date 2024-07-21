count = 2
n = int(input())
for i in range(n): 
    for j in range(n):
        print(count, end=" ")
        count += 2
        if count == 10:
            count = 2
    print()