count_3 = 0
count_5 = 0
for i in range(10):
    a = int(input())
    if a%3 == 0:
        count_3 += 1
    if a%5 == 0:
        count_5 += 1
print(count_3, count_5)