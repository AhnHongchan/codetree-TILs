n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

min_v = float('inf')  # 최소값을 찾기 위해 초기값을 무한대로 설정합니다.
for i in range(n):
    sum_v = 0
    for j in range(1, n):
        # 이동한 거리 j에 대해 모듈러 연산을 적용하여 인덱스 오버플로우를 방지합니다.
        next_room = (i + j) % n
        sum_v += a[next_room] * j
    min_v = min(min_v, sum_v)

print(min_v)