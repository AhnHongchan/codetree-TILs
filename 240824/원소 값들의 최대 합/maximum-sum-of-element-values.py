def max_sum(n, m, sequence):
    max_total = 0
    
    for start in range(n):
        current_pos = start
        current_sum = 0
        
        for _ in range(m):
            current_sum += sequence[current_pos]
            current_pos = sequence[current_pos] - 1
        
        max_total = max(max_total, current_sum)
    
    return max_total

# 입력
n, m = map(int, input().split())
sequence = list(map(int, input().split()))

# 최대 합 계산
result = max_sum(n, m, sequence)
print(result)