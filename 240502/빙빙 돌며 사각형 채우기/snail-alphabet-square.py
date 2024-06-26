n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

dx, dy = [0,1,0,-1],[1,0,-1,0]
cnt = 65
start = 65
x, y = 0, 0
d = 0
arr[x][y] = chr(start)

while cnt < 65 + n * m - 1:
    nx = x + dx[d]
    ny = y + dy[d]    
    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
        x = nx
        y = ny
        start += 1
        cnt += 1
        arr[x][y] = chr(start)
    else:
        d = (d+1) % 4
    
    if start == 90:
        start = 64

for lst in arr:
    print(*lst)