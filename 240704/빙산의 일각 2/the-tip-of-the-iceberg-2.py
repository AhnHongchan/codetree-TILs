n = int(input())

# 빙산 값
ice = [int(input()) for _ in range(n)]

ans = 0

for i in range(1, 1001):
    rest_ice = [x - i for x in ice]
    cnt = 0
    in_chunk = False
    for height in rest_ice:
        if height > 0:
            if not in_chunk:
                cnt += 1
                in_chunk = True
        else:
            in_chunk = False
    ans = max(ans, cnt)

print(ans)