# 북에서부터 시계 방향으로 회전
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

order = input()
cnt = 0
x, y = 0, 0
for i in range(len(order)):
    if order[i] == 'L':
        cnt = (cnt-1) % 4
    elif order[i] == 'R':
        cnt =(cnt+1) % 4
    else:
        x += dx[cnt]
        y += dy[cnt]

print(x, y)