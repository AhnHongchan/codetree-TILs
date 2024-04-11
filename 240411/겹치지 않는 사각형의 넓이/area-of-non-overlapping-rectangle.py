center = 1000
arr = [[0] * (2*center+1) for _ in range(2*center+1)]

for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(center+x1, center+x2):
        for y in range(center+y1, center+y2):
            arr[x][y] = 1

x1, y1, x2, y2 = map(int, input().split())
for x in range(center+x1, center+x2):
    for y in range(center+y1, center+y2):
        arr[x][y] = 2

cnt = 0
for x in range(2*center+1):
    for y in range(2*center+1):
        if arr[x][y] == 1:
            cnt += 1

print(cnt)