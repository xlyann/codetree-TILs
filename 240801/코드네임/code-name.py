class codename:
    def __init__(self, name, score):
        self.name = name
        self.score = score

agent = []
for i in range(5):
    a, b = input().split()
    b = int(b)
    agent.append(codename(a, b))

min_name = ''
min_val = 100
for i in range(5):
    new = agent[i]
    if new.score < min_val:
        min_val = new.score
        min_name = new.name

print(min_name, min_val)