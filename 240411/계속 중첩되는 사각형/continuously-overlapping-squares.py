n = int(input())
arr = [[0] * 201 for _ in range(201)]

cnt = 0
while cnt < n:
    cnt += 1
    x1, y1, x2, y2 = map(int, input().split())
    if cnt % 2 == 1:
        for i in range(100+x1, 100+x2):
            for j in range(100+y1, 100+y2):
                arr[i][j] = 1
    else:
        for i in range(100+x1, 100+x2):
            for j in range(100+y1, 100+y2):
                arr[i][j] = 2

cnt_v = 0
for x in range(201):
    for y in range(201):
        if arr[x][y] == 2:
            cnt_v += 1

print(cnt_v)