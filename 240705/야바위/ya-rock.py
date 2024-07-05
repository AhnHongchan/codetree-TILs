n = int(input())

# n번의 교환 정보 (a, b, c)
cases = [tuple(map(int, input().split())) for _ in range(n)]

# 1번, 2번, 3번 컵 중 어디에 처음에 조약돌을 놓을지 시뮬레이션
max_score = 0

for initial_position in range(1, 4):
    current_position = initial_position  # 조약돌의 현재 위치
    score = 0
    
    for a, b, c in cases:
        # a번과 b번 컵을 교환
        if current_position == a:
            current_position = b
        elif current_position == b:
            current_position = a
        
        # c번 컵을 열어 확인
        if current_position == c:
            score += 1
    
    # 최대 점수를 업데이트
    max_score = max(max_score, score)

print(max_score)