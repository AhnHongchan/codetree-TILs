n = int(input())
location = []

for _ in range(n):
    x, y = map(int, input().split())
    location.append((x,y))

ans = 1000000
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = location[i]
        x2, y2 = location[j]
        length = (x1 - x2) ** 2 + (y1 - y2) ** 2
        ans = min(ans, length)

print(ans)