n, c, g, h = map(int, input().split())
standards = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for num in range(1001):
    cnt = 0
    for standard in standards:
        low, high = standard
        if num < low:
           cnt += c
        elif low <= num < high:
            cnt += g
        else:
            cnt += h
    ans = max(ans, cnt)

print(ans)