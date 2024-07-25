n = int(input())
length = 0
count_a = 0
for i in range(n):
    ex = input()
    length += len(ex)
    if ex[0] == 'a':
        count_a += 1

print(length, count_a)