count_12 = 0
count_3 = 0
count_2 = 0
a = int(input())
for i in range(1, a+1):
    if i % 12 == 0:
        count_12 += 1
    elif i % 3 == 0:
        count_3 += 1
    elif i % 2 == 0:
        count_2 += 1

print(count_2, count_3, count_12)