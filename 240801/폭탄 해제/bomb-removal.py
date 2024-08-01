class bomb:
    def __init__(self, code, color, s):
        self.code = code
        self.color = color
        self.s = s

    def clear(self, code, color, s):
        print('code :', self.code)
        print('color :', self.color)
        print('second :', self.s)

a, b, c = input().split()
need = bomb(a, b, c)
need.clear(a, b, c)