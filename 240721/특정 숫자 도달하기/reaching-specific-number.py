a = list(map(int, input().split()))
c = True

for i in a:
    if i >= 250:
        b = a.index(i)
        c = False
        break
if c == False:
    a = a[:-(len(a)-b)]
print(sum(a), '{:.1f}'.format(sum(a)/len(a)))