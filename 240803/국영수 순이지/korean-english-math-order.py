class subject:
    def __init__(self, name, kor, eng, math):
        self.name, self.kor, self.eng, self.math = name, kor, eng, math

save = []
n = int(input())
for i in range(n):
    a, b, c, d = input().split()
    save.append(subject(a, int(b), int(c), int(d)))

save.sort(key=lambda x : (-x.kor, -x.eng, -x.math))

for j in save:
    print(j.name, j.kor, j.eng, j.math)