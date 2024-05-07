N = int(input())
numbers = list(map(int, input().split()))

count = 0

# 가능한 모든 구간을 확인
for start in range(N):
    for end in range(start + 1, N + 1):
        # 현재 구간의 원소들을 추출
        subarray = numbers[start:end]
        
        # 구간의 평균값 계산
        average = sum(subarray) / len(subarray)
        
        # 구간 안에 있는 원소가 평균값과 정확히 일치하는지 확인
        if average in subarray:
            count += 1
            continue

print(count)