sat = True
for i in range(5):
    a = int(input())
    if a%3 != 0:
        sat = False
        break

print(sat*1)