a = list(input())
while len(a) != 1:
    cut = int(input())
    if cut >= len(a):
        a.pop()
    else:
        a.pop(cut)
    print(''.join(a))