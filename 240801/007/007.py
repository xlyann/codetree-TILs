class _007:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time

a, b, c = input().split()
new = _007(a, b, c)

print('secret code :', new.code)
print('meeting point :', new.point)
print('time :', new.time)