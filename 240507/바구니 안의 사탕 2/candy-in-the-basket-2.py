# 입력 받기
N, K = map(int, input().split())
buckets = []
for _ in range(N):
    candies, position = map(int, input().split())
    buckets.append((candies, position))

# 사탕의 수가 최대가 되는 경우 찾기
max_candies = 0
for center in range(101):
    candies_sum = 0
    for candies, position in buckets:
        if abs(center - position) <= K:
            candies_sum += candies
    max_candies = max(max_candies, candies_sum)

# 결과 출력
print(max_candies)