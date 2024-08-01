a = input()
new_a = list(a)
b = input()
new_b = list(b)
new_a.sort()
new_b.sort()
if new_a == new_b:
    print('Yes')
else:
    print("No")