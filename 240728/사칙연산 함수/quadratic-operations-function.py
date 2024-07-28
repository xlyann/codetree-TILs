def cal(a, o, c):
    if o == '+':
        return print(a, '+', c, '=', a+c) 

    if o == '-':
        return print(a, '-', c, '=', a-c)

    if o == '*':
        return print(a, '*', c, '=', a*c) 

    if o == '/':
        return print(a, '/', c, '=', a//c) 
    
    return print(False)

a, o, c = input().split()
cal(int(a), o, int(c))