clean = [0]*101
a,b = map(int, input().split())
c,d = map(int, input().split())

for i in range(a,b):
    clean[i] = 1
for i in range(c,d):
    clean[i] = 1
print(clean.count(1))