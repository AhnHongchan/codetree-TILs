n = int(input())

# 빙산 값

ice = [int(input()) for _ in range(n)]

ans = 0
for i in range(1, 1001):
    rest_ice = [x-i for x in ice]
    cnt = 0
    for j in range(n):
        if j != n-1:
            if rest_ice[j] > 0 and rest_ice[j+1] <=0 and j+1 < n:
                cnt += 1
        else:
            if rest_ice[j-1] <= 0 and rest_ice[j] > 0:
                cnt += 1
    ans = max(ans, cnt)

print(ans)