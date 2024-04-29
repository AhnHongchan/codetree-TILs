n, m = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr = [[0] * m for _ in range(n)]
cnt = 1
d = 0
x, y = 0, 0
arr[x][y] = cnt

while cnt < n * m:
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
        x = nx
        y = ny
        cnt += 1
        arr[x][y] = cnt
    else:
        d = (d + 1) % 4

for lst in arr:
    print(*lst)