class product:
    def __init__(self, name = 'codetree', code = '50'):
        self.name = name
        self.code = code
    
new_1 = product()
print(f'product {new_1.code} is {new_1.name}')

a, b = input().split()
new_2 = product(a, b)
print(f'product {new_2.code} is {new_2.name}')