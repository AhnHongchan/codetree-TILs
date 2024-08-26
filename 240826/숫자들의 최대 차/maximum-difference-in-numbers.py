# 입력 받기
N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]

# 리스트 정렬
lst.sort()

# 투 포인터를 활용하여 최적의 부분집합을 찾기
left = 0
max_count = 0

for right in range(N):
    while lst[right] - lst[left] > K:
        left += 1
    max_count = max(max_count, right - left + 1)

# 결과 출력
print(max_count)