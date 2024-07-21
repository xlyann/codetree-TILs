n = int(input())
for i in range(n): 
    for j in range(n):
        print((1+i) * (n-j), end=" ")
    print()