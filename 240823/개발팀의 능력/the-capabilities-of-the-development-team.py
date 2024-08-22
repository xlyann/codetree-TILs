num = list(map(int, input().split()))
ans = 9999999
cnt = 0

for i in range(5):
    for j in range(5):
        for k in range(j+1, 5):
            if i == j or i == k:
                continue
            team_1 = num[i]
            team_2 = num[j] + num[k]
            team_3 = sum(num) - team_1 - team_2
            if team_1 != team_2 and team_2 != team_3 and team_3 != team_1:
                diff = max(team_1, team_2, team_3) - min(team_1, team_2, team_3)
                ans = min(ans, diff)
                cnt += 1
if cnt == 0:
    print(-1)
else:
    print(ans)