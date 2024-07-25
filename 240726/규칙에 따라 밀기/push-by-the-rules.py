target = input()
com = input()
for i in com:
    if i == 'L':
        target = target[1:] + target[0]
    else:
        target = target[-1] + target[:-1]
print(target)