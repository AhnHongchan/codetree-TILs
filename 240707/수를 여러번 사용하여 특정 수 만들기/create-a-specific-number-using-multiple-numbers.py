def find_max_sum(A, B, C):
    max_sum = 0
    
    # A를 0번부터 가능한 최대 횟수만큼 더해보기
    for i in range(C // A + 1):
        current_sum = A * i
        remaining = C - current_sum
        
        # 남은 값으로 B를 몇 번 더할 수 있는지 계산
        max_B_count = remaining // B
        total_sum = current_sum + B * max_B_count
        
        # 가장 큰 값을 갱신
        if total_sum <= C:
            max_sum = max(max_sum, total_sum)
    
    return max_sum

A, B, C = map(int, input().split())
# 함수 호출 및 결과 출력
result = find_max_sum(A, B, C)
print(result)  # 출력: 76