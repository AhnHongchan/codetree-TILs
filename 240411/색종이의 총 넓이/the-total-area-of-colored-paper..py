n = int(input())
arr = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+8):
        for j in range(y, y+8):
            arr[i][j] = 1

cnt = 0
for x in range(101):
    for y in range(101):
        if arr[x][y] == 1:
            cnt += 1

print(cnt)