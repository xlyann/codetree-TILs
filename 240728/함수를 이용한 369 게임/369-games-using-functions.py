def in_3(num):
    num = str(num)
    for i in num:
        if i in ['3', '6', '9']:
            return True
    return False

def mul_3(num):
    return num%3 == 0

count = 0
a, b = map(int, input().split())

for i in range(a, b+1):
    if in_3(i) or mul_3(i):
        count += 1

print(count)