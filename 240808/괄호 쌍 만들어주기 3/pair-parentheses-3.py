a=list(input())

ans=0
for i in range(len(a)):
    for j in a[i:]:
        if a[i]+j=='()':
            ans+=1

print(ans)