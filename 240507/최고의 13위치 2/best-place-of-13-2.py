n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

# 1 * 3 크기의 격자를 가로로 배치하는 경우
for x in range(n):
    for y in range(n - 2):
        cnt = 0
        for z in range(3):
            cnt += arr[x][y + z]

        # 두 번째 격자를 배치하는 경우
        for a in range(n):
            for b in range(n - 2):
                if a == x and (b == y or b == y + 1 or b == y + 2):  # 겹치지 않게 조건 추가
                    continue
                else:
                    cnt2 = 0
                    for z in range(3):
                        cnt2 += arr[a][b + z]
                    val = cnt + cnt2
                    ans = max(ans, val)

print(ans)