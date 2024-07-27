a, b = input().split()

def find(string):
    new = ''
    for i in string:
        if i.isdigit():
            new += i
        else:
            break
    return int(new)

print(find(a) + find(b))