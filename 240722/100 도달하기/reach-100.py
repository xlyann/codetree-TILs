a = int(input())
num = [1, a]
count = 1
new = 1+a
while True:
    if new>100:
        break
    new = num[count-1] + num[count]
    num.append(new)
    count += 1
print(*num)