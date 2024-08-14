A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

offset = - min(min(A_list), min(B_list))
limit = max(max(A_list), max(B_list)) + offset

coordi = list([0]*limit for _ in range(limit))

def paint(a, b, c, d, num):
    global offset
    for i in range(a + offset, c + offset):
        for j in range(b + offset, d + offset):
            coordi[i][j] = num

paint(*A_list, 1)
paint(*B_list, 0)

count_x = 0
count_y = 0
for find_1 in coordi:
    new = find_1.count(1)
    if new > 0:
        count_x += 1
    
    if count_y < new:
        count_y = new   

print(count_x * count_y)