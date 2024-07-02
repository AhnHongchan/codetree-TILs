n = int(input())
location = []

for _ in range(n):
    x, y = map(int, input().split())
    location.append((x, y))

ans = 0
for i in range(n):
    x1, y1 = location[i]
    for j in range(i+1, n):
        x2, y2 = location[j]
        for k in range(j+1, n):
            x3, y3 = location[k]
            tri = abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3))
            ans = max(ans, tri)

print(ans)