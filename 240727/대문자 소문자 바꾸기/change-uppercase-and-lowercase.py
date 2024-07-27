a = input()
# print(a.swapcase())
for i in a:
    if i >= 'A' and i <= 'Z':
        print(i.lower(), end = '')
    else:
        print(i.upper(), end = '')