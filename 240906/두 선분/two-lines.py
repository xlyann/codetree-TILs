a, b, c, d = map(int, input().split())
if b<c or d<a:
    print('nonintersecting')
else:
    print('intersecting')