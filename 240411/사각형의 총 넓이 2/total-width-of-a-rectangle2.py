n = int(input())
center = 100
square = [[0] * (2 * center + 1) for _ in range(2 * center + 1)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(center+x1, center+x2):
        for j in range(center+y1, center+y2):
            square[i][j] = 1

cnt = 0 
for x in range(2 * center + 1):
    for y in range(2 * center + 1):
        if square[x][y] == 1:
            cnt += 1

print(cnt)