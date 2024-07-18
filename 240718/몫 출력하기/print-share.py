count = 0
while True:
    a = int(input())
    if a%2 == 0:
        print(a//2)
        count += 1
    if count == 3:
        break