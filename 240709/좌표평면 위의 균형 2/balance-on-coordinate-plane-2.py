n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

ans = 10000

for i in range(0, 101, 2):
    for j in range(0, 101, 2):
        x1, y1 = i, j
        count = [0] * 5
        for k in range(n):
            x2 = points[k][0]
            y2 = points[k][1]
            if x2 > x1 and y2 > y1:
                count[1] += 1
            elif x2 > x1 and y2 < y1:
                count[2] += 1
            elif x2 < x1 and y2 < y1:
                count[3] += 1
            else:
                count[4] += 1
        cnt = max(count)
        ans = min(ans, cnt)

print(ans)