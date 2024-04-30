order = input()
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
k = 0
cnt = 0

for d in order:
    if d == 'F':
        x += dx[k]
        y += dy[k]

    elif d == 'L':
        k = (k-1) % 4

    else:
        k = (k+1) % 4

    cnt += 1
    
    if x == 0 and y == 0:
        print(cnt)
        break
else:
    print(-1)