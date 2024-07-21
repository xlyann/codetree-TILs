n, m = map(int, input().split())
for i in range(1, 10): 
    for j in range(m, n-1, -2):
        print(f"{j} * {i} = {i * j}", end="")
        if j > n:
            print(" / ", end="")
    print()