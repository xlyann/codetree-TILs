n = int(input())
_list = list(map(int, input().split()))

def lcm(a, b):
    if a<b:
        a, b = b, a
    
    if b == 0:
        return a

    return lcm(b, a%b)

def gcm(a, b):
    return a*b//lcm(a, b)

num = 1
for i in range(n):
    num = gcm(num, _list[i])

print(num)