num = list(map(int, input().split()))
ans = 9999999

for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            for l in range(k+1, 6):
                num_4 = [num[i], num[j], num[k], num[l]]
                except_num = sum(num) - sum(num_4)
                for a in range(4):
                    for b in range(a+1, 4):
                        sum_num_1 = num_4[a] + num_4[b]
                        sum_num_2 = sum(num_4) - sum_num_1
                        diff = max(except_num, sum_num_1, sum_num_2) - min(except_num, sum_num_1, sum_num_2)
                        ans = min(ans, diff)
print(ans)