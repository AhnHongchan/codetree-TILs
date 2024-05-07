n, m = map(int, input().split())
arr = [input() for _ in range(n)]
cnt = 0
dxs, dys = [1, 0, -1, 0, 1, 1, -1, -1], [0, 1, 0, -1, 1, -1, 1, -1]

for x in range(n):
    for y in range(m):
        if arr[x][y] != 'L':
            continue
        for dx, dy in zip(dxs, dys):
            found = True
            nx, ny = x, y
            for _ in range(2):  # 'LEE'의 두 번째와 세 번째 문자인 'E'를 확인
                nx += dx
                ny += dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m or arr[nx][ny] != 'E':
                    found = False
                    break
            if found:
                cnt += 1

print(cnt)