a = input()
new = a[-1] + a[:-1]
print(a)
while new != a:
    print(new)
    new = new[-1] + new[:-1]
print(a)