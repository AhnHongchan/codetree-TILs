n = int(int(input()))
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = 0
for x in range(len(arr)):
    for y in range(len(arr)):
        cnt = 0
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1:
                    cnt += 1
        if cnt >= 3:
            result += 1

print(result)