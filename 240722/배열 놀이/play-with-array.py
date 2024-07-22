a, b = map(int, input().split())
num = list(map(int, input().split()))
for i in range(b):
    com = input()
    if com.startswith('1'):
        print(num[int(com.split()[1])-1])
    elif com.startswith('2'):
        find = int(com.split()[1])
        if find in num:
            print(num.index(find)+1)
        else:
            print(0)
    elif com.startswith('3'):
        s, e = int(com.split()[1]), int(com.split()[2])
        print(*num[s-1:e])