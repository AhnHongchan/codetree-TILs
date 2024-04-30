n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
cnt = 1
arr[0][0] = cnt
x, y = 0, 0
# 하, 우, 상, 좌
dx, dy = [1,0,-1,0], [0,1,0,-1]
d = 0

while cnt < n * m:
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
        x = nx
        y = ny
        cnt += 1
        arr[x][y] = cnt
    else:
        d = (d+1) % 4

for lst in arr:
    print(*lst)