n = int(input())
location = []
for _ in range(n):
    x, y = map(int, input().split())
    location.append((x, y))

ans = 40000 ** 2

for i in range(n):
    # x, y좌표를 하나씩 추가한다.
    x_val = []
    y_val = []
    for j in range(n):
        # 하나 제외
        if j == i:
            continue
        else:
            x1, y1 = location[j]
            x_val.append(x1)
            y_val.append(y1)
    
    # 받은 좌표에서 좌표당 최소, 최대 좌표 구하기
    x_min = min(x_val)
    y_min = min(y_val)
    x_max = max(x_val)
    y_max = max(y_val)
    
    # 모든 점들을 포함하는 직사각형을 그리려면 최대값에서 최소값을 뺀 길이들을 곱하면 된다.
    sqr = (x_max - x_min) * (y_max - y_min)
    ans = min(ans, sqr)

print(ans)