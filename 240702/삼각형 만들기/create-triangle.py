def max_rectangle_area(n, points):
    max_area = 0
    
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            if x1 == x2 or y1 == y2:
                continue
            for k in range(n):
                x3, y3 = points[k]
                if x3 == x1 and y3 == y2:
                    area = abs((x2 - x1) * (y2 - y1))
                    max_area = max(max_area, area)
                elif x3 == x2 and y3 == y1:
                    area = abs((x2 - x1) * (y2 - y1))
                    max_area = max(max_area, area)
    
    return max_area

# 입력 받기
n = int(input().strip())
points = [tuple(map(int, input().strip().split())) for _ in range(n)]

# 최대 넓이의 두 배 출력
result = max_rectangle_area(n, points)
print(result)