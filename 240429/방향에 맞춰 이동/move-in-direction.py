N = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
move = {
    'E':0,
    'N':1,
    'W':2,
    'S':3
    }

x, y = 0, 0
for i in range(N):
    direction, num = input().split()
    num = int(num)
    x = x + dx[move[direction]] * num
    y = y + dy[move[direction]] * num

print(x, y)