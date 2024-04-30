N = int(input())
x, y = 0, 0
dx, dy = [0,1,0,-1], [1,0,-1,0]
polar = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3,
}

cnt = 0
stop = False
for i in range(N):
    # d는 방향, w는 거리
    d, w = input().split()
    w = int(w)
    
    for j in range(w):
        x += dx[polar[d]]
        y += dy[polar[d]]
        cnt += 1
        if x == 0 and y == 0:
            stop = True
            break
    if stop:
        print(cnt)
        break

    elif i == N-1 and not stop:
        print(-1)