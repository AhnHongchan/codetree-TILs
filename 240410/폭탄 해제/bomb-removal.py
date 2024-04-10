class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

a, b, c = tuple(input().split())
bomb = Bomb(a, b, c)
print(f'code : {bomb.code}')
print(f'color : {bomb.color}')
print(f'second : {bomb.second}')