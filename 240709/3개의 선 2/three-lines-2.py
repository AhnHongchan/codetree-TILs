from itertools import combinations

def can_cover_all_points_with_three_lines(points):
    x_coords = set()
    y_coords = set()
    
    for x, y in points:
        x_coords.add(x)
        y_coords.add(y)
    
    x_coords = list(x_coords)
    y_coords = list(y_coords)
    
    # 1. 세 개의 수직선으로 모든 점 커버 가능한지 확인
    if len(x_coords) <= 3:
        return 1
    
    # 2. 세 개의 수평선으로 모든 점 커버 가능한지 확인
    if len(y_coords) <= 3:
        return 1
    
    # 3. 혼합된 경우 확인 (x선 1개 + y선 2개, x선 2개 + y선 1개)
    for x_comb in combinations(x_coords, 1):
        for y_comb in combinations(y_coords, 2):
            covered = all(x in x_comb or y in y_comb for x, y in points)
            if covered:
                return 1
    
    for x_comb in combinations(x_coords, 2):
        for y_comb in combinations(y_coords, 1):
            covered = all(x in x_comb or y in y_comb for x, y in points)
            if covered:
                return 1
    
    return 0

# 입력 받기
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(can_cover_all_points_with_three_lines(points))