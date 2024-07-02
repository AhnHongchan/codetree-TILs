n = int(input())
points = []

for i in range(n):
    a, b = map(int, input().split())
    points.append((a, b))

ans = n

for i in range(n):
    x, y = points[i]
    for j in range(n):
        if j == i:
            continue
        if x < points[j][0] and y > points[j][1]:
            ans -= 1
            pass
        elif x > points[j][0] and y < points[j][1]:
            ans -= 1
            pass
            
print(ans)