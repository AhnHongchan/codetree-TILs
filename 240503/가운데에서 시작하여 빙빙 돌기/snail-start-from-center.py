n = int(input())
arr = [[0] * n for _ in range(n)]
dx, dy = [0,-1,0,1], [-1,0,1,0]
x = n-1
y = n-1
d = 0
start = n ** 2
arr[x][y] = start

while start > 1:
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
        x = nx
        y = ny
        start -= 1
        arr[x][y] = start
    else:
        d = (d+1) % 4

for lst in arr:
    print(*lst)