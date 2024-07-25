string, n = input().split()
new = list(string)
for i in range(int(n)):
    num, first, second = input().split()
    if num == '1':
        _1 = int(first)-1
        _2 = int(second)-1
        new[_1], new[_2] = new[_2], new[_1]
        print(''.join(new))
    else:
        for i in range(len(new)):
            if new[i] == first:
                new[i] = second
        print(''.join(new))