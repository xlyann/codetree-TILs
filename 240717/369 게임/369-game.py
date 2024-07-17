a = int(input())
for i in range(1, a+1):
    if i % 3 == 0:
        print(0, end = ' ')
    else:
        count = 0
        for j in str(i):
            if j in ['3', '6', '9']:
                print(0, end = ' ')
                break
            else:
                count += 1
        if count == len(str(i)):
            print(i, end = ' ')