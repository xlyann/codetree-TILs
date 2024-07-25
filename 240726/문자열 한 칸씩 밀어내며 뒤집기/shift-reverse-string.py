target, n = input().split()
for i in range(int(n)):
    req = input()
    if req == '1':
        target = target[1:] + target[0]
    if req == '2':
        target = target[-1] + target[:-1]
    if req == '3':
        target = target[::-1]
    print(target)