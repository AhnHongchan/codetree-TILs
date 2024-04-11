ctr = 1000
arr = [[0] * (2*ctr+1) for _ in range(2*ctr+1)]

x1, y1, x2, y2 = map(int, input().split())
for i in range(ctr+x1, ctr+x2):
    for j in range(ctr+y1, ctr+y2):
        arr[i][j] = 1

x1, y1, x2, y2 = map(int, input().split())
for i in range(ctr+x1, ctr+x2):
    for j in range(ctr+y1, ctr+y2):
        arr[i][j] = 0

min_x = 2001
min_y = 2001
max_x = 0
max_y = 0

# 1인 경우 x,y의 최대 좌표와  최소 좌표를 구해보자
square = False
for i in range(2*ctr+1):
    for j in range(2*ctr+1):
        if arr[i][j] == 1:
            square = True
            max_x = max(max_x, i)
            max_y = max(max_y, j)
            min_x = min(min_x, i)
            min_y = min(min_y, j)

area = 0

if not square :
    area = 0
else :
    area = (max_x-min_x+1) * (max_y- min_y+1)

print(area)