a = input()
new = list(a)
new[1] = 'a'
new[-2] = 'a'
print(''.join(new))