def min_max_value_on_path(n, k, arr):
    # 초기값 설정
    dp = [float('inf')] * n
    dp[0] = arr[0]  # 1번 돌에서 시작

    # 동적 프로그래밍을 통한 최소 최댓값 계산
    for i in range(1, n):
        # i번 돌에 도달하기 위한 이전 돌 j의 가능한 범위 (i-k 부터 i-1 까지)
        for j in range(max(0, i - k), i):
            dp[i] = min(dp[i], max(dp[j], arr[i]))

    # 결과값 출력
    return dp[-1]

# 입력 예제
n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(min_max_value_on_path(n, k, arr))