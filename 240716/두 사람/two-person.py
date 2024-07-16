age1, s1 = input().split()
age2, s2 = input().split()
if (int(age1) < 19 or s1 == 'W') and (int(age2) < 19 or s2 == 'W'):
    print(0)
else:
    print(1)