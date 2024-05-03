N, T = map(int, input().split())
order = input()
arr = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1,0,1,0],[0,1,0,-1]
x, y = (N-1)//2, (N-1)//2
d = 0
sum_v = arr[x][y]
for i in range(T):
    if order[i] == 'F':
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            x = nx
            y = ny
            sum_v += arr[x][y]
    elif order[i] == 'R':
        d = (d+1) % 4

    else:
        d = (d-1) % 4

print(sum_v)