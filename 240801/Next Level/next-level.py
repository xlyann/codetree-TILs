class Level:
    def __init__(self, ID = 'codetree', level = 10):
        self.ID = ID
        self.level = level

new_1 = Level()
print('user {0} lv {1}'.format(new_1.ID, new_1.level))

a, b = tuple(input().split())
new_2 = Level(a, b)
print('user {0} lv {1}'.format(new_2.ID, new_2.level))