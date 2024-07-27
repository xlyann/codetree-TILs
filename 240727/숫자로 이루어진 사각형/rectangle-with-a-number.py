def rec_num(n):
    count = 1
    for i in range(n):
        for j in range(n):
            print(count, end = ' ')
            count += 1
            if count == 10:
                count = 1
        print()

a = int(input())
rec_num(a)