a = input()
for i in a:
    if i.isalpha():
        print(i.lower(), end = '')
    elif i.isdigit():
        print(i, end = '')