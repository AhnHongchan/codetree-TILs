N, M = map(int, input().split())
arr = [[0]* N for _ in range(N)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

for i in range(M):
    r, c = map(int, input().split())
    x = r-1
    y = c-1
    arr[x][y] = 1
    cnt = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == 1:
                cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)