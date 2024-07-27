def find_num(string):
    new = ''
    for i in string:
        if i.isdigit():
            new += i
    return int(new)

a = input()
b = input()

print(find_num(a)+find_num(b))