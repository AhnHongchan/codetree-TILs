n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    count = [0] * 1001
    for j in range(n):
        if i == j:
            continue
        x, y = times[j]
        for j in range(x, y):
            count[j] += 1

    cnt = 0
    for k in range(len(count)):
        if count[k] != 0:
            cnt += 1

    ans = max(ans, cnt)

print(ans)