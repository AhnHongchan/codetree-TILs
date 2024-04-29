n, t = map(int, input().split())

r, c, d = input().split()
x = int(r)
y = int(c)

dx = [0, -1, 0, 1]  # 상하좌우 순서로 이동하기 위한 x 좌표 변화량
dy = [-1, 0, 1, 0]  # 상하좌우 순서로 이동하기 위한 y 좌표 변화량

time = 0
while time < t:
    # 현재 위치에서 이동 방향에 따라 이동할 좌표 변화량 계산
    if d == 'L':
        cnt = 0
    elif d == 'R':
        cnt = 2
    elif d == 'U':
        cnt = 1
    else:  # d == 'D'
        cnt = 3

    # 이동한 후의 좌표 계산
    nx = x + dx[cnt]
    ny = y + dy[cnt]

    # 이동한 좌표가 범위를 벗어나면 벽에 부딪혔다는 의미이므로 이동 방향을 반대로 변경
    if nx < 1 or ny < 1 or nx > n or ny > n:
        if d == 'L':
            d = 'R'
        elif d == 'R':
            d = 'L'
        elif d == 'U':
            d = 'D'
        else:  # d == 'D'
            d = 'U'
    else:  # 이동한 좌표가 범위 내에 있을 경우에만 좌표 갱신
        x = nx
        y = ny

    # 1초 증가
    time += 1

# 최종 위치 출력
print(x, y)