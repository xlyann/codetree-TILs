count = 0
save = []
while True:
    a = input()
    if a == '0':
        break
    count += 1
    if count%2 == 1:
        save.append(a)
print(count)
print('\n'.join(save))